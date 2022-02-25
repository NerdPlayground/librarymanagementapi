from django.urls import path
from students.views import StudentAPIView

urlpatterns= [
    path('students/',StudentAPIView.as_view(),name='students')
]