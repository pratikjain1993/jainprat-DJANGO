from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls import patterns
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers
from passenger_requests import urls
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
urlpatterns = patterns('',(r'^', include('example.urls')))