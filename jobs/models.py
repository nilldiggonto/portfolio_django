from django.db import models
from datetime import datetime

#Model Create

class Job(models.Model):
    image   = models.ImageField(upload_to='images/job/%y/%m/%d')
    summary = models.CharField(max_length=200)