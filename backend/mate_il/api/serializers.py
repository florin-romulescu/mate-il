from rest_framework import serializers
from .models import Post, Announce

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'description',
                  'created_at', 'image', 'attachments',
                  'external_url']

class AnnounceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announce
        fields = ['id', 'title', 'author', 'content', 'created_at']
        