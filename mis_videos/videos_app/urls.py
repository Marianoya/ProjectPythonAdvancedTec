from django.urls import path
from . import views

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
    path('user/register/confirmacion', views.user_registration, name='user_registration'),
]


