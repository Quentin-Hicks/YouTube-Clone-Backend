from rest_framework import serializers
from .models import Reply

class ReplySerializer(serializers.ModelSerializer):
   class Meta:
      model = Reply
      fields = ['comment_id', 'comment', 'text', 'user_id'] 
      depth = 1