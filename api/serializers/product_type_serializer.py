from django.contrib.auth.models import User
from api.models import *
from rest_framework import serializers

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ProductType
        fields = '__all__'