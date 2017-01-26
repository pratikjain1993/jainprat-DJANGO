from django.db import models


class Trip_Request(models.Model):
    request_id = models.CharField(max_length=20, primary_key=True)
    status = models.CharField(max_length=5)
    driver_id = models.CharField(max_length=20)

    def as_json(self):
        return dict(
            request_id=self.request_id,
            status = self.status,
            driver_id = self.driver_id)
