from .models import Product
from rest_framework import serializers

class ProductsSerializers(serializers.ModelSerializers):
    class Meta:
        model = Product
        fields = '__all__'