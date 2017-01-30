from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email= serializers.EmailField()
    pic = serializers.FileField()
    phone = serializers.IntegerField()
    home_add= serializers.CharField(max_length=100)
    carno= serializers.CharField(max_length=100)
    identity = serializers.FileField()
    password = serializers.CharField(max_length=100)
    rating = serializers.DecimalField(max_digits=4, decimal_places=2)
