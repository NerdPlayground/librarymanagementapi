from django.urls import path
from categories.views import CategoryAPIView

urlpatterns= [
    path('categories/',CategoryAPIView.as_view(),name='categories')
]