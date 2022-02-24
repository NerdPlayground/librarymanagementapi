from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from books.serializers import BookSerializer
from books.models import Book

class BookAPIView(APIView):
    def get(self, request):
        books= Book.objects.all()
        serializer= BookSerializer(books,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request):
        data= request.data
        serializer= BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)