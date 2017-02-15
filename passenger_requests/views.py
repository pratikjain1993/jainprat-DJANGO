import json
from driver import driver
from passenger_requests.serializers import Trip_Request
from passenger_requests.models import User
from testing.serializers import UserSerializer
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def checkproof(request):
    if request.method == 'POST':
        Id = request.POST.get('id')
        checkuser = User.objects.get(id=Id)
        print checkuser.carno
        print checkuser.identity
        if checkuser.carno is not None and checkuser.identity != "":
            return Response("1")
        else:
            return Response("0")


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def checkmatch(request):
    if request.method == 'POST':
        id = request.POST.get('email')
        pwd = request.POST.get('pass')
        try:
            checkuser = User.objects.get(email=id)
        except ObjectDoesNotExist:
            checkuser = None
        print checkuser
        if checkuser is None:
            return Response("nouser")

        elif checkuser is not None:
            if pwd == checkuser.password:
                response_data = {}
                response_data['id'] = checkuser.id
                response_data['name'] = checkuser.name
                return Response(response_data)
            else:
                return Response("nomatch")


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def register(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        Homeadd = request.POST.get('homeadd')
        Carno = request.POST.get('carno')
        Pw = request.POST.get('pass')
        user_obj = User()
        user_obj.name = Name
        user_obj.email = Email
        user_obj.phone = Phone
        user_obj.home_add = Homeadd
        user_obj.carno = Carno
        user_obj.password = Pw
        user_obj.rating = 0.0
        user_obj.save(force_insert=True)
        return Response("success")

#curl -X POST -F id=7 -F slat=ew -F slong=q -F dlat=eww -F dlong -F ts=ewww  192.168.1.103:8000/api/request


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def passenger_request(request):
    request_id = request.data['id']
    newRequest = Trip_Request()
   # req = UserSerializer.objects.get(id = request_id)
    driver(request_id)
    req = User.objects.get(id = request_id)
    newRequest.request_id = request_id
    newRequest.status = "101"
    newRequest.driver_id = "NULL"
    newRequest.source_lat = request.data['slat']
    newRequest.source_long = request.data['slong']
    newRequest.destination_lat= request.data['dlat']
    newRequest.destination_long= request.data['dlong']
    newRequest.timestamp= request.data['ts']
    newRequest.name = req.name
    newRequest.phone_no = req.phone
    newRequest.save()
    string = driver(request_id)

    return HttpResponse(string)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def get_passenger(request):
    Id = request.data['id']
    req = Trip_Request.objects.get(request_id=Id)
    return HttpResponse(json.dumps(req.as_json()), content_type="application/json")


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def get_status(request): #Function to return status of request, polled continously by passenger's app
    Id = request.data['id']
    req = Trip_Request.objects.get(request_id = Id)
    return HttpResponse(json.dumps(req.as_json()), content_type="application/json")


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def get_driver(request): #Function to return driver id is called when status=303 ie driver is found
    Id = request.data['id']
    req = Trip_Request.objects.get(request_id = Id)
    return Response(req.driver_id)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def driver_response(request):
    passenger_id = request.data['request_id']
    req = Trip_Request.objects.get(request_id = passenger_id)
    req.driver_id = request.data['id']
    req.driver_lat = request.data['lat']
    req.driver_long = request.data['long']
    req.status = 202
    req.save()
    return HttpResponse("Done")


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def endjourney(request):  # Function to finish journey, called when the passenger reaches its destination
    Id = request.data['id']
    req = Trip_Request.objects.get(request_id=Id)
    req.status = 404
    req.save()
    return HttpResponse("Done")


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def finish(request): # Function to delete request record called after completion of request when driver id is received by passenger's app
    Id = request.data['id']
    Trip_Request.objects.get(request_id = Id).delete()
    return HttpResponse("Done")


def checkmatch(request):
        if request.method == 'POST':
            id = request.POST.get('email', '')
            pwd = request.POST.get('pass', '')
            checkuser = UserSerializer.objects.all().filter(email=id)
            if pwd == checkuser.password:
                return Response(status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def getuser(request):
        Id = request.data['id']
        req = UserSerializer.objects.get(pk=Id)
        return HttpResponse(json.dumps(req.as_json()), content_type="application/json")




