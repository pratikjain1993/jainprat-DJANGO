from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls import patterns
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from passenger_requests.views import passenger_request,get_status,get_driver,get_passenger, driver_response, complete
from testing.views import checkmatch,register,checkproof,picupload,forgetpass
from example.estimatedFareCalculationModule import getEstFare
from example.actualFareCalculationModule import getActFare
from driver_request.views import driver_request, player_id, end_journey, driver_complete
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
    url(r'^checkmatch$', checkmatch),
    url(r'^register$', register),
    url(r'^checkproof$', checkproof),
    url(r'^picupload$', picupload),
    url(r'^forgetpass$', forgetpass),

    url(r'^driver_request', driver_request),
    url(r'^player_id', player_id),
    url(r'^endjourney', end_journey),
    url(r'^driver_complete', driver_complete),

    url(r'^api/request', passenger_request),
    url(r'^api/status', get_status),
    url(r'^api/driver', get_driver),
    url(r'^api/response', driver_response),
    url(r'^api/complete', complete),
    url(r'^api/get_passenger',get_passenger),
    url(r'^api/estimatefare', getEstFare),
    url(r'^api/actualfare', getActFare)
]