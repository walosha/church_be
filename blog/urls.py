from django.urls import path, include
from .views import PostListCreateAPIView, PostRetrieveAPIView, PostDestroyAPIView, PostUpdateAPIView, CommentListCreateAPIView, CommentRetrieveAPIView, CommentDestroyAPIView, CommentUpdateAPIView

urlpatterns = [
    path('posts/<uuid:pk>/', PostRetrieveAPIView.as_view(),
         name="Post_detail"),
    path('posts/', PostListCreateAPIView.as_view(), name="post_list"),
    path('posts/<uuid:pk>/', PostUpdateAPIView.as_view(), name="post_update"),
    path('posts/<uuid:pk>/', PostDestroyAPIView.as_view(),
         name="post_delete"),
    path('coments/<uuid:pk>/', CommentRetrieveAPIView.as_view(),
         name="comment_detail"),
    path('coments/', CommentListCreateAPIView.as_view(), name="comment_list"),
    path('coments/<uuid:pk>/', CommentUpdateAPIView.as_view(), name="comment_update"),
    path('coments/<uuid:pk>/', CommentDestroyAPIView.as_view(),
         name="event_delete"),
]
