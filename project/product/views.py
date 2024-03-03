from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer
from .permissions import *


# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [StudentAccessToProduct]