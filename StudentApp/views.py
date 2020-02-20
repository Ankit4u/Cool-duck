from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from StudentApp.models import Result, Users
from StudentApp.serializers import LoginSerializer


class LoginView(APIView):

    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    @csrf_exempt
    def post(self, request):
      user = request.data.get('user',{})
      print(user)
      serializer = self.serializer_class(data=user)
      serializer.is_valid(raise_exception=True)
      return Response(serializer.validated_data, status=status.HTTP_200_OK)

# def Data(request):
#     result_obj =0
#     if request.role == 1 :
#         result_obj = Result.objects.all()
#     if request.role == 2 :
#         result=Result.objects.filter(student__Name=request.user)