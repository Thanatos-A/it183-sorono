from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet

class viewPosts(ModelViewSet):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

@api_view(['GET'])
def viewPostDetail(request, pk):
    try:
        post = get_object_or_404(Post, id=pk)
        serializer = PostSerializer(post, many=False)
        return Response(serializer.data, status=HTTP_200_OK)
    except NotFound:
        return Response({"error": "Post not found"}, status=HTTP_404_NOT_FOUND)

@api_view(['POST'])
def addPost(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['PUT'])  # Correct method for updating a resource
def updatePost(request, pk):
    try:
        post = get_object_or_404(Post, id=pk)
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    except NotFound:
        return Response({"error": "Post not found"}, status=HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deletePost(request, pk):
    try:
        post = get_object_or_404(Post, id=pk)
        post.delete()
        return Response({"message": "Post deleted successfully"}, status=HTTP_200_OK)
    except NotFound:
        return Response({"error": "Post not found"}, status=HTTP_404_NOT_FOUND)
