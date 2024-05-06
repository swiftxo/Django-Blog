from django.urls import path
from .views import RegisterUser,EditUser,ChangePassword, ProfilePage,EditProfilePage
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', RegisterUser.as_view(), name = 'register'),
    path('personal_info/', EditUser.as_view(), name = 'personal_info'),
    path('<int:uid>/password/', ChangePassword.as_view(), name = 'change-password'),
    path('password_success', views.password_success, name = 'password_success'),
    path('<int:pk>/profile',ProfilePage.as_view(),name = "show_profile_page"),
    path('<int:pk>/edit_profile',EditProfilePage.as_view(),name = "edit_profile"),



]
