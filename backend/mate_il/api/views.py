from django.shortcuts import render
from rest_framework import generics
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

@api_view(['GET'])
def post_search(request):
    pass

class AnnounceList(generics.ListAPIView):
    queryset = Announce.objects.all()
    serializer_class = AnnounceSerializer

class AnnounceDetail(generics.RetrieveAPIView):
    queryset = Announce.objects.all()
    serializer_class = AnnounceSerializer   

@api_view(['GET'])
def announce_search(request):
    pass