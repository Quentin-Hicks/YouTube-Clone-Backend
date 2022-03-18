from rest_framework import serializers
from .models import Reply, Song

class SongSerializer(serializers.ModelSerializer):
   class Meta:
      
      model = Reply
      fields = ['id', 'user', 'comment', 'text', 'user_id'] 
      depth = 1 