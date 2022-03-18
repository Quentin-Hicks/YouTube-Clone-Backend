from django.contrib.auth.models import User
 
from django.db import models


# Create your models here.
class Reply(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey
    text = models.CharField(max_length=1000)
 