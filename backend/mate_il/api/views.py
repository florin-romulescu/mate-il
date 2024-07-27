from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from .models import Post, Announce
from .serializers import PostSerializer, AnnounceSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

def search_util(request, queryset, serializer_cls):
    q = request.query_params.get('q', None)
    author = request.query_params.get('author', None)
    tags = request.query_params.get('tags', None)
    created_after = request.query_params.get('created_after', None)
    created_before = request.query_params.get('created_before', None)

    if q:
        queryset = queryset.filter(title__icontains=q)
    if author:
        queryset = queryset.filter(author__icontains=author)
    if tags:
        tag_list = tags.split(',')
        queryset = queryset.filter(tags__name__in=tag_list).distinct()
    if created_after:
        queryset = queryset.filter(created_at__gte=created_after)
    if created_before:
        queryset = queryset.filter(created_at__lte=created_before)
    
    serializer = serializer_cls(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

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
    queryset = Post.objects.all()
    return search_util(request, queryset, PostSerializer)
    

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
    queryset = Announce.objects.all()
    return search_util(request, queryset, AnnounceSerializer)