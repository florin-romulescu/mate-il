from django.urls import path
from .views import PostList, PostDetail, post_search, AnnounceList, AnnounceDetail, announce_search, post_tags, TagList, TagDetail, tag_posts

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('posts/<int:pk>/tags/', post_tags, name='post-tags'),
    path('posts/search/', post_search, name='post-search'),
    path('announces/', AnnounceList.as_view(), name='announce-list'),
    path('announces/<int:pk>/', AnnounceDetail.as_view(), name='announce-detail'),
    path('announces/search/', announce_search, name='announce-search'),
    path('tags/', TagList.as_view(), name='tag-list'),
    path('tags/<int:pk>/', TagDetail.as_view(), name='tag-detail'),
    path('tags/<int:pk>/posts/', tag_posts, name='tag-posts'),
]