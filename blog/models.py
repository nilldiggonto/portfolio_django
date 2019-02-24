from django.db import models
from datetime import datetime
# Create your models here.
class Blog(models.Model):
    title       = models.CharField(max_length=250)
    pub_date    = models.DateTimeField()
    body        = models.TextField()
    image       = models.ImageField(upload_to='images/blog/%y/%m/%d')

    def __str__(self):
        return self.title
    


