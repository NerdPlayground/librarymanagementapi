from django.http import Http404
from rest_framework import status
from patrons.models import Patron
from rest_framework.response import Response
from rest_framework.decorators import APIView
from patrons.serializers import PatronSerializer,RegisterSerializer

class PatronAPIView(APIView):
    def get(self,request):
        patrons= Patron.objects.all()
        serializer= PatronSerializer(patrons,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data= request.data
        serializer= RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)