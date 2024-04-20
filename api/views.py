from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import PostSerializer
from posts.models import Post

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/posts'},
        {'GET': '/api/post/id'},
        {'POST': '/api/post/id/like'},
        {'POST': '/api/post/id/dislike'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},
    ]

    return Response(routes)

@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPost(request, pk):
    posts = Post.objects.get(id=pk)
    serializer = PostSerializer(posts, many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postLike(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user.profile
    
    if user in post.liked_by.all():
        return Response({'message': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        post.liked_by.add(user)
        post.likes += 1
        post.save()
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postDislike(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user.profile

    if user not in post.liked_by.all():
        return Response({'message': 'You have not liked this post yet.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        post.liked_by.remove(user)
        post.likes -= 1
        post.save()
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)