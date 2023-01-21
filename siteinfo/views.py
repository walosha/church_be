from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import generics
# from django.db.models import Count


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveAPIView(generics.RetrieveAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDestroyAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
