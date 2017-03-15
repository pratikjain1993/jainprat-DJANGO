from django.shortcuts import render
from models import Driver_Request
from passenger_requests.models import Trip_Request
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def driver_request(request):
    newRequest = Driver_Request()
    newRequest.request_id = request.data['id']
    newRequest.source_lat = request.data['slat']
    newRequest.source_long = request.data['slong']
    newRequest.destination_lat= request.data['dlat']
    newRequest.destination_long= request.data['dlong']
    newRequest.timestamp= request.data['ts']
    newRequest.save()
    return HttpResponse("Done")

@api_view(['GET','POST'])
@permission_classes((permissions.AllowAny,))
def player_id(request):
    Id = request.data['id']
    req = Driver_Request.objects.get(request_id=Id)
    req.player_id = request.data['player_id']
    req.save()
    return HttpResponse("Done")



@api_view(['GET','POST'])
@permission_classes((permissions.AllowAny,))
def end_journey(request): # Function to delete request record called after completion of request when driver id is received by passenger's app
    Id = request.data['id']
    req = Trip_Request.objects.get(request_id=Id)
    req.status = 404
    req.save()
    return HttpResponse("Done")

@api_view(['GET','POST'])
@permission_classes((permissions.AllowAny,))
def driver_complete(request): # Function to delete request record called after completion of request when driver id is received by passenger's app
    Id = request.data['id']
    Driver_Request.objects.get(request_id = Id).delete()
    return HttpResponse("Done")
