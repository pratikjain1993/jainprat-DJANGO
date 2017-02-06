from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
import json
from driver import driver
from passenger_requests.serializers import Trip_Request
from testing.serializers import UserSerializer


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def passenger_request(request):
    request_id = request.data['id']
    timestamp = request.data['ts']
    source = request.data['src']
    destination = request.data['dest']
    newRequest = Trip_Request()
   # req = UserSerializer.objects.get(id = request_id)
    driver(request_id)

    newRequest.request_id = request_id
    newRequest.status = "101"
    newRequest.driver_id = "NULL"
    newRequest.source = source
    newRequest.destination= destination
    newRequest.timestamp= timestamp
    #newRequest.name = req.name
    #newRequest.phone_no = req.phone
    newRequest.save()
    return HttpResponse("Done")

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
    return Response(req.status)

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def get_driver(request): #Function to return driver id is called when status=303 ie driver is found
    Id = request.data['id']
    req = Trip_Request.objects.get(request_id = Id)
    return Response(req.driver_id)

def driver_response(request):
    passenger_id = request.data['request_id']
    driver_id = request.data['id']
    req = Trip_Request.objects.get(request_id = passenger_id)
    req.driver_id = driver_id
    req.status = 202
    req.save()


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def finish(request): # Function to delete request record called after completion of request when driver id is received by passenger's app
    Id = request.data['id']
    Trip_Request.objects.get(request_id = Id).delete()
    return HttpResponse("Done")




