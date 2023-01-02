from django.db import models


class Subscription(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    location = models.CharField(max_length=100)
    weather_conditions = models.TextField()
    is_active = models.BooleanField(default=True)
