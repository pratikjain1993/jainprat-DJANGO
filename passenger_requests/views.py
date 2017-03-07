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


#curl -X POST -F id=7 -F slat=ew -F slong=q -F dlat=eww -F dlong -F ts=ewww  192.168.1.103:8000/api/request

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def passenger_request(request):
    request_id = request.data['id']
    newRequest = Trip_Request()
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
def complete(request): # Function to delete request record called after completion of request when driver id is received by passenger's app
    Id = request.data['id']
    Trip_Request.objects.get(request_id = Id).delete()
    return HttpResponse("Done")








