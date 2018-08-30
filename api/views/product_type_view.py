from django.contrib.auth.models import User
from rest_framework import viewsets
from django.core import serializers

from api.models import *
from api.serializers import *

class ProductTypeViewSet(viewsets.ModelViewSet):
    '''API endpoint allows product type to be viewed or edited'''

    queryset = ProductType.objects.all().order_by("name")
    serializer_class = ProductTypeSerializer


