from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from passenger_requests.views import passenger_request
from passenger_requests.views import get_status
from passenger_requests.views import get_driver
from passenger_requests.views import finish
from passenger_requests.views import get_passenger
from passenger_requests.views import driver_response
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


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/request', passenger_request),
    url(r'^api/status', get_status),
    url(r'^api/driver', get_driver),
    url(r'^api/response', driver_response),
    url(r'^api/complete', finish),
    url(r'^api/get_passenger', get_passenger)

]