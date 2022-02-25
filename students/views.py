from django.http import Http404
from rest_framework import status
from students.models import Student
from rest_framework.response import Response
from rest_framework.decorators import APIView
from students.serializers import StudentSerializer

class StudentAPIView(APIView):
    def get(self,request):
        students= Student.objects.all()
        serializer= StudentSerializer(students,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        data= request.data
        serializer= StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)