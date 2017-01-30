from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from testing.serializers import UserSerializer
import json

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
    req = UserSerializer.objects.get(pk = Id)
    return HttpResponse(json.dumps(req.as_json()), content_type="application/json")




	

		
