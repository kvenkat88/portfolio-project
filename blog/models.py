from django.db import models
from django.utils.timezone import datetime


class Blog(models.Model):
    title = models.CharField(max_length = 255,blank=False)
    pub_date = models.DateTimeField()#default=datetime.now()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')


