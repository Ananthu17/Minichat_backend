from django.shortcuts import render,get_object_or_404
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import permissions
from rest_framework.generics import (ListAPIView,RetrieveAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView)


            
class Registerview(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def post(self,request):
        received_data=json.loads(request.body)
        user=User.objects.create_user(username=received_data['username'],password=received_data['password'])
        user.save()
        serilazer = Userserializer(user)
        return Response(serilazer.data)
        
class UserListView(ListAPIView):
    serializer_class = Userserializer
    permission_classes = (permissions.AllowAny, )
    def get_queryset(self):
        queryset = User.objects.all()
        return queryset


class ChatRetriveView(APIView):
    serializer_class = ChatSerializer
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def post(self,request):
        received_data=json.loads(request.body)
        user = User.objects.get(username=received_data["user"])
        friend = User.objects.get(username=received_data["friend"])
        chat = Chat.objects.filter(participants=user).filter(participants=friend)
        if not chat:
            chat = Chat()
            chat.save()
            chat.participants.add(user,friend)
        serilazer = ChatSerializer(chat,many=True)
        return Response(serilazer.data)

def get_last_10_messages(chatId):
    chat = get_object_or_404(Chat, id=chatId)
    return chat.messages.order_by('-timestamp').all()[:10]


def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    return user

def get_current_chat(chatId):
    return get_object_or_404(Chat, id=chatId)

