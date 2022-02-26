from django.http import Http404
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import APIView
from patrons.serializers import UserSerializer,RegisterSerializer,LoginSerializer

class LoginAPIView(APIView):
    def post(self,request):
        username= request.data.get('username')
        password= request.data.get('password')
        user= authenticate(username=username,password=password)

        if user is not None:
            serializer= LoginSerializer(user=user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'message':'Invalid Credentials'},status=status.HTTP_401_UNAUTHORIZED)

class UserAPIView(APIView):
    def get(self,request):
        patrons= User.objects.all()
        serializer= UserSerializer(patrons,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data= request.data
        serializer= RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)