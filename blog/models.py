from django.db import models
from datetime import datetime
# Create your models here.
class Blog(models.Model):
    title       = models.CharField(max_length=250)
    pub_date    = models.DateTimeField()
    body        = models.TextField()
    image       = models.ImageField(upload_to='images/blog/%y/%m/%d')


    def summary(self):
        return self.body[:100]


    def publish_date(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
    


