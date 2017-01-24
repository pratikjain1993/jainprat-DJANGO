from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def checkmatch(request):
    if request.method == 'POST':
        id= request.POST.get('email', '')
        pwd= request.POST.get('pass', '')
        checkuser = User.objects.all().filter(email=id)
        if pwd == checkuser.password:
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

			
	

		
