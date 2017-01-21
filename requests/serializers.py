from rest_framework import serializers
from requests.models import Trip_Request


class TripRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip_Request
        fields = ('request_id','status','driver_id')