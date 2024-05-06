from django.urls import path
from .views import Home,Article,CreatePost,EditPost,DeletePost,CreateCategory,CategoryView, Likes

urlpatterns = [
  path('', Home.as_view(), name="home"),
  path ('article/<int:pk>' , Article.as_view(), name = "article-detail"),
  path('new_post/', CreatePost.as_view(),  name = 'create_post'),  
  path('article/<int:pk>/edit',EditPost.as_view(), name = 'edit_post' ),
  path('article/<int:pk>/delete',DeletePost.as_view(), name = 'delete_post' ),
  path('create_category/', CreateCategory.as_view(),  name = 'create_category'),  
  path('category/<str:cats>/',CategoryView, name = 'category' ),
  path('like/<int:pk>', Likes, name = 'like_post'),


]
