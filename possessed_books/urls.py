from django.urls import path
from possessed_books.views import PossessedBookAPIView

urlpatterns= [
    path('checkout/',PossessedBookAPIView.as_view(),name='checkout'),
]