from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls import patterns
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from passenger_requests import views as pviews
from testing import views as testingviews
from example.views import ListCreateTestClass
from example.estimatedFareCalculationModule import getEstFare
from example.actualFareCalculationModule import getActFare

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^checkmatch$', testingviews.checkmatch, name='checkmatch'),
    url(r'^register$', testingviews.register, name='register'),
    url(r'^checkproof$', testingviews.checkproof, name='checkproof'),
    url(r'^picupload$', testingviews.picupload, name='picupload'),
    url(r'^forgetpass$', testingviews.forgetpass, name='forgetpass'),
    url(r'^api/request', pviews.passenger_request),
    url(r'^api/status', pviews.get_status),
    url(r'^api/driver', pviews.get_driver),
    url(r'^api/response', pviews.driver_response),
    url(r'^api/endjourney', pviews.endjourney ),
    url(r'^api/complete', pviews.complete),
    url(r'^api/get_passenger', pviews.get_passenger),
    url(r'^api/estimatefare', getEstFare),
    url(r'^api/actualfare', getActFare)
]