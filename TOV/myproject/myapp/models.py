from django.db import models

class Subscriber(models.Model):
    name = models.CharField(max_length=100)