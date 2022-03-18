from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    users = models.ForeignKey(User,on_delete=models.CASCADE)
    video_id = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    likes = models.IntegerField()
    dislikes = models.IntegerField()