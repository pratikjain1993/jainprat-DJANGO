from django.db import models


class Trip_Request(models.Model):
    request_id = models.CharField(max_length=20, primary_key=True)
    status = models.CharField(max_length=5)
    driver_id = models.CharField(max_length=20)
    source = models.CharField(max_length=200)
    destination = models.CharField(max_length=20)
    timestamp = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=200)

    def as_json(self):
        return dict(
            request_id=self.request_id,
            status = self.status,
            driver_id = self.driver_id,
            source = self.source,
            destination = self.destination,
            timestamp = self.timestamp,
            name = self.name,
            phone_no = self.phone_no)
