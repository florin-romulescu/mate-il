from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from .models import Post, Announce
from .serializers import PostSerializer, AnnounceSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Post.DoesNotExist:
            raise NotFound(detail="Post with the given ID was not found.")

@api_view(['GET'])
def post_search(request):
    pass

class AnnounceList(generics.ListAPIView):
    queryset = Announce.objects.all()
    serializer_class = AnnounceSerializer

class AnnounceDetail(generics.RetrieveAPIView):
    queryset = Announce.objects.all()
    serializer_class = AnnounceSerializer

    def get_object(self):
        try:
            return super().get_object()
        except Announce.DoesNotExist:
            raise NotFound(detail="Announce with the given ID was not found.")

@api_view(['GET'])
def announce_search(request):
    pass