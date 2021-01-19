from django.urls import path,include

from store.api.views import ProductListAPIView
from store.api.views import ProductDetailAPIView





urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product_list_create'),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name='product_rud')
]