from django.urls import path
from .views import ProductPost, ProductDeleteGet

urlpatterns = [
    path('product/', ProductPost.as_view(), name='product-post'),
    path('product/<int:id>', ProductDeleteGet.as_view(), name='produc-espc'),
]
