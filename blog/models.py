from django.db import models
from datetime import datetime
from django.urls import reverse
from .utils import unique_slug_generator
from django.db.models.signals import pre_save

# Create your models here.
class Blog(models.Model):
    title       = models.CharField(max_length=250)
    slug        = models.CharField(max_length=250, null=True,blank=True)
    pub_date    = models.DateTimeField()
    body        = models.TextField()
    image       = models.ImageField(upload_to='images/blog/%y/%m/%d')


    def summary(self):
        return self.body[:100]


    def publish_date(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})
    


def blog_slug_presave_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(blog_slug_presave_receiver,sender=Blog)
    


