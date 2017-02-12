

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics, permissions
from testing.models import User
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
        user_obj.save(force_insert=True)
        return Response("success")










	

		
