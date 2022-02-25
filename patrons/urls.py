from django.urls import path
from patrons.views import PatronAPIView

urlpatterns= [
    path('patrons/',PatronAPIView.as_view(),name='patrons')
]