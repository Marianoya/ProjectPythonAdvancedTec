"""
URL configuration for mis_videos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from videos_app import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('video/<int:pk>/', views.video_view, name='video_view'),
    path('video/new/', views.video_add, name='video_add'),
    path('video/<int:pk>/edit/', views.video_edit, name='video_edit'),
    path('video/<int:pk>/delete/', views.video_delete, name='video_delete'),

    path('user/<int:pk>/', views.user_view, name='user_view'),
    path('user/new/', views.user_add, name='user_add'),
    path('user/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('user/<int:pk>/delete/', views.user_delete, name='user_delete'),

    path('user/register/', views.user_registration, name='user_registration'),
    path('user/register/confirmacion/', views.confirmacion, name='confirmacion'),
    path('user/register/confirmacion/confirmacionexitosa/', views.confirmacion_exitosa, name='confirmacion_exitosa'),
]
