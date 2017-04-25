from django.conf.urls import url
from . import views

urlpatterns = [
    #/home/
    url(r'^$', views.index, name='index'),


]