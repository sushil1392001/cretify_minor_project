from django.db import models


class Messagee(models.Model):
    reciver_id= models.IntegerField()
    sender_id=models.IntegerField()
    messages= models.CharField(max_length=200)

