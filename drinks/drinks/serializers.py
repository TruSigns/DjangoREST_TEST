# Description python object to JSON
from rest_framework import serializers
from .models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    # metadata to describe models

    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']