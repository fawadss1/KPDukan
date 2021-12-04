from rest_framework import serializers
from . import models


class SpSerliazer(serializers.ModelSerializer):
    class Meta:
        model = models.Simple_Product
        fields = '__all__'


class VpSerliazer(serializers.ModelSerializer):
    class Meta:
        model = models.Variety_Product
        # fields = ('Name')
        fields = '__all__'
