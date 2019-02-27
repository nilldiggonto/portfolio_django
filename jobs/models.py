from django.db import models
from datetime import datetime
from django.utils import timezone

#Model Create

class Job(models.Model):
    image   = models.ImageField(upload_to='images/job/%y/%m/%d')
    summary = models.CharField(max_length=200)


class ContactUser(models.Model):
    user        = models.CharField(max_length=120,blank=True,null=True)
    email       = models.CharField(max_length=100,blank=True,null=True)
    content     = models.TextField(blank=True,null=True)
    send_date   = models.DateTimeField(null=True,default=timezone.now)

    def __str__(self):
        return self.user
    