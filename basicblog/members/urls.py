from django.urls import path, include
from .views import UserRegisterView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
