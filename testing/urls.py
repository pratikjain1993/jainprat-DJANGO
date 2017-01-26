from django.conf.urls import url, include

from . import views
urlpatterns = [
   
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^checkmatch$', views.checkmatch, name='checkmatch'),
    url(r'^getuser$', views.getuser, name='getuser')

]