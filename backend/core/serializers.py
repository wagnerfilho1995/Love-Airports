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

class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aircraft
        fields = [
            "model",
            "manufacturer"
        ]
    
class ItinerarySerializer(serializers.ModelSerializer):
    aircraft = AircraftSerializer(many=False, read_only=True)
    class Meta:
        model = Itinerary
        fields = [
            "departure_time",
            "arrival_time",
            "fare_price",
            "aircraft"
        ]

class TravelSerializer(serializers.ModelSerializer):
    origin = AirportSerializer(many=False, read_only=True)
    destination = AirportSerializer(many=False, read_only=True)
    itinerary = ItinerarySerializer(many=False, read_only=True)
    class Meta:
        model = Travel
        fields = [
            "departure_date",
            "origin",
            "destination",
            "currency",
            "itinerary"
        ]

class SuitableSerializer(serializers.ModelSerializer):
    aircraft = AircraftSerializer(many=False, read_only=True)
    class Meta:
        model = Suitable
        fields = [
            "url",
            "dist",
            "cost",
            "aircraft"
        ]