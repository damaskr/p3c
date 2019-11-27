from django.db import models

# Create your models here.

class Afterseoul(models.Model):
    school_name = models.CharField(max_length=20)
    location = models.CharField(max_length=10)
    employ_type = models.CharField(max_length=10)
    school_url = models.CharField(max_length=100)
