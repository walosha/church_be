from .models import Post, Comment, Publication
from .serializers import PostSerializer, CommentSerializer, PublicationSerializer
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


# Commment
class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentUpdateAPIView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDestroyAPIView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Publications


class PublicationCreateAPIView(generics.CreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class PublicationListAPIView(generics.ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class PublicationRetrieveAPIView(generics.RetrieveAPIView):

    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class PublicationUpdateAPIView(generics.UpdateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class PublicationDestroyAPIView(generics.DestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
