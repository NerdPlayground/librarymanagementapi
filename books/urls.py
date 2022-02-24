from django.urls import path
from books.views import BookAPIView

urlpatterns= [
    path('books/',BookAPIView.as_view(),name='books')
]