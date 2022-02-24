from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from categories.serializers import CategorySerializer
from categories.models import Category

class CategoryAPIView(APIView):
    def get(self, request):
        books= Category.objects.all()
        serializer= CategorySerializer(books,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        data= request.data
        serializer= CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)