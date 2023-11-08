from django.shortcuts import render
from .serializers import ProductsSerializers
from .models import Product
from rest_framework import viewsets


# Create your views here.

class ProductView(viewsets.ModelsViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializers
