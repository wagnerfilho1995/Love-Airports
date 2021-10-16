from rest_framework import serializers
from .models import *

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = [
            "iata",
            "city",
            "lat",
            "lon",
            "state"
        ]