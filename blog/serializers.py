# django #selenium #webscraping
from rest_framework import serializers
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.UUIDField()

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.UUIDField()

    class Meta:
        model = Post
        fields = ('title', "author", "slug", "comments", "tags", "status")


class PublicationSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = serializers.UUIDField()

    class Meta:
        model = Comment
        fields = '__all__'
