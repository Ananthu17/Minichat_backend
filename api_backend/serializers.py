from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from . import views

class Tokenserializers(serializers.ModelSerializer):
    class Meta :
        model= Token
        fields = '__all__'

class Userserializer(serializers.ModelSerializer):
    class Meta :
        model= User
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'


  
    