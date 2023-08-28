from django.shortcuts import render
from .models import User, Chat, Message, PDFDocument, UserHistory

def chat_list(request):
    # Retrieve a list of chats
    chats = Chat.objects.all()
    return render(request, 'chatapp/chat_list.html', {'chats': chats})

def chat_detail(request, chat_id):
    # Retrieve details of a specific chat
    chat = Chat.objects.get(pk=chat_id)
    return render(request, 'chatapp/chat_detail.html', {'chat': chat})

def user_profile(request, user_id):
    # Retrieve user profile details
    user = User.objects.get(pk=user_id)
    user_history = UserHistory.objects.get(user=user)
    return render(request, 'chatapp/user_profile.html', {'user': user, 'user_history': user_history})

