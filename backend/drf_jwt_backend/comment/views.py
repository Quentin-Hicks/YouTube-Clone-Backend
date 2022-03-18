from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import CommentSerializer
from .models import Comment
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

 # handles calling the complete comment list


@api_view(['GET'])
def comment_list(request):
    comments_param = request.query_params.get('video_id')
    sort_param = request.query_params.get('sort')
    comment = Comment.objects.all()
    if comments_param:
        comment = comment.filter(video_id=comments_param)
    elif sort_param:
        comment = comment.order_by(sort_param)
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_comments(request):
    print('User ', f"{request.user.id} {request.user.email} {request.user.username}")
    if request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.



