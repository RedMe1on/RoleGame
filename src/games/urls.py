from django.urls import path
from .views import GamesListView, GamesDetailView, PostCreateView, PostListView, PostDetailView

urlpatterns = [
    path('games/', GamesListView.as_view(), name='games_list'),
    path('games/<int:pk>/', GamesDetailView.as_view(), name='games_detail'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
