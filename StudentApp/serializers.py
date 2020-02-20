from django.contrib.auth import authenticate, login
from rest_framework import serializers
from .models import User, Users


class LoginSerializer(serializers.Serializer):
  username = serializers.CharField(max_length=100)
  password= serializers.CharField(max_length=100)
  def validate(self, data):
    username = data.get("username", None)
    password = data.get("password", None)
    if username is None:
      raise serializers.ValidationError("Username Required")
    if password is None:
      raise serializers.ValidationError("Password is required")
    auth_user = authenticate(username=username,password=password)
    # print(auth_user)
    if auth_user is None:
      raise serializers.ValidationError("User Not Found")
    return {
       "user":str(auth_user),
       "token":auth_user.token
    }


