from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import ReplySerializer
from .models import Reply
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_reply(request):
    if request.method == 'GET':
        print('okay reply')
        reply_param = request.query_params.get('user_id')
        sort_param = request.query_params.get('sort')
        reply = Reply.objects.all()
        if reply_param:
            reply = reply.filter(user_id =reply_param)
        elif sort_param:
            reply = reply.order_by(sort_param)
        serializer = ReplySerializer(reply, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
   