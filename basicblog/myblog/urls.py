# from . import views
from django.urls import path
from .views import (
    HomeView,
    ArticleDetailView,
    AddPostView,
    ContactView,
    UpdatePostView,
    DeletePostView,
    AddCategoryView,
    CategoryView,
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('', views.home, name="home"),
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    path("add_post/", AddPostView.as_view(), name="add_post"),
    path("add_category/", AddCategoryView.as_view(), name="add_category"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("article/edit/<int:pk>", UpdatePostView.as_view(), name="update_post"),
    path("article/<int:pk>/delete/", DeletePostView.as_view(), name="delete_post"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("category/", CategoryView.as_view(), name="category"),
]
