from django.urls import path, include
from .views import PostCreateAPIView, PostListAPIView, PostRetrieveAPIView, PostDestroyAPIView, PostUpdateAPIView, CommentListCreateAPIView, CommentRetrieveAPIView, CommentDestroyAPIView, CommentUpdateAPIView, PublicationCreateAPIView, PublicationListAPIView, PublicationRetrieveAPIView, PublicationDestroyAPIView, PublicationUpdateAPIView

urlpatterns = [
    path('posts/<uuid:pk>/', PostRetrieveAPIView.as_view(),
         name="Post_detail"),
    path('posts/create/', PostCreateAPIView.as_view(), name="post_create"),
    path('posts/', PostListAPIView.as_view(), name="post_list"),
    path('posts/<uuid:pk>/', PostUpdateAPIView.as_view(), name="post_update"),
    path('posts/<uuid:pk>/', PostDestroyAPIView.as_view(),
         name="post_delete"),
    path('coments/<uuid:pk>/', CommentRetrieveAPIView.as_view(),
         name="comment_detail"),
    path('coments/', CommentListCreateAPIView.as_view(), name="comment_list"),
    path('coments/<uuid:pk>/', CommentUpdateAPIView.as_view(), name="comment_update"),
    path('coments/<uuid:pk>/', CommentDestroyAPIView.as_view(),
         name="event_delete"),
    path('posts/<uuid:pk>/', PublicationRetrieveAPIView.as_view(),
         name="publication_detail"),
    path('publication/create/', PublicationCreateAPIView.as_view(),
         name="publication_create"),
    path('publication/', PublicationListAPIView.as_view(), name="publication_list"),
    path('publication/<uuid:pk>/', PublicationUpdateAPIView.as_view(),
         name="publication_update"),
    path('publication/<uuid:pk>/', PublicationDestroyAPIView.as_view(),
         name="publication_delete"),
]
