from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import APIView
from possessed_books.models import PossessedBook
from rest_framework.permissions import IsAuthenticated
from possessed_books.serializers import PossessedBookSerializer

class PossessedBookAPIView(APIView):
    permission_classes= [IsAuthenticated]
    def get(self,request):
        possessed_books= PossessedBook.objects.all()
        serializer= PossessedBookSerializer(possessed_books,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data= request.data
        serializer= PossessedBookSerializer(data=data)
        if serializer.is_valid():
            serializer.save(student=self.request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
