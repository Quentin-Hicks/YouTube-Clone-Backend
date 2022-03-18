from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
<<<<<<< HEAD
    users = models.ForeignKey(User, on_delete=models.CASCADE)
=======
    users = models.ForeignKey(User,on_delete=models.CASCADE)
>>>>>>> 67cbade0de7f8db68e4643d5482512ae93667c74
    video_id = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)