from __future__ import unicode_literals
from django.db import models


class Trip_Request(models.Model):
    request_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=5)
    driver_id = models.CharField(max_length=20)
    driver_lat = models.CharField(max_length=200)
    driver_long = models.CharField(max_length=200)
    source_lat = models.CharField(max_length=200)
    source_long = models.CharField(max_length=200)
    destination_lat = models.CharField(max_length=200)
    destination_long = models.CharField(max_length=200)
    timestamp = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)

    def as_json(self):
        return dict(
            request_id=self.request_id,
            status = self.status,
            driver_id = self.driver_id,
            source_lat=self.source_lat,
            source_long=self.source_long,
            destination_lat=self.destination_lat,
            destination_long = self.destination_long,
            driver_lat =self.driver_lat,
            driver_long = self.driver_long,
            timestamp = self.timestamp,
            name = self.name,
            phone_no = self.phone_no)



class User(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        pic = models.FileField()
        phone = models.IntegerField()
        home_add = models.TextField()
        carno = models.CharField(max_length=100)
        identity = models.FileField()
        password = models.CharField(max_length=100)
        rating = models.DecimalField(max_digits=4, decimal_places=2)

        def __unicode__(self):
            return self.email

        def as_json(self):
            return dict(
                name=self.name,
                email=self.email,
                pic=self.pic,
                phone=self.phone,
                home_add=self.home_add,
                carno=self.carno,
                identity=self.identity,
                password=self.password,
                rating=self.rating
            )
