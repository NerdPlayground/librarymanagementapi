from django.urls import path
from patrons.views import UserAPIView,LoginAPIView

urlpatterns= [
    path('login/',LoginAPIView.as_view(),name='login'),
    path('patrons/',UserAPIView.as_view(),name='patrons'),
]