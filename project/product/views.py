from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer
from .permissions import *


# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [StudentAccessToProduct]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return ProductSerializer