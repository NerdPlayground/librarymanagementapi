from django.urls import path
from patrons.views import PatronAPIView,LoginAPIView

urlpatterns= [
    path('patrons/',PatronAPIView.as_view(),name='patrons'),
    path('login/',LoginAPIView.as_view(),name='login')
]