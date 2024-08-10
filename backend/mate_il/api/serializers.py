from rest_framework import serializers
from .models import Post, Announce, Tag

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'description',
                  'created_at', 'image', 'has_attachment',
                  'external_url']

class AnnounceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announce
        fields = ['id', 'title', 'author', 'content', 'created_at']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
        