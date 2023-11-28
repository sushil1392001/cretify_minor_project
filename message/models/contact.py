from django.db import models
import datetime


class Contact(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    user_messages = models.CharField(max_length=500)
    datetime = models.DateTimeField(default=datetime.datetime.now())
