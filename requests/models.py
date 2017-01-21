from django.db import models


class Trip_Request(models.Model):
    request_id = models.CharField(max_length=20, primary_key=True)
    status = models.CharField(max_length=5)
    driver_id = models.CharField(max_length=20)
