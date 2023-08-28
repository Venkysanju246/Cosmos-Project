from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('chat/<int:chat_id>/', views.chat_detail, name='chat_detail'),
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
    # Add more URL patterns for your other views here
]
