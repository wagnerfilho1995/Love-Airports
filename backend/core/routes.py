from rest_framework import routers, serializers, viewsets
from rest_framework.routers import DefaultRouter
from . import viewsets

'''
Setting Endpoints.
'''

router = DefaultRouter()

router.register(r'airports', viewsets.AirportViewSet)
router.register(r'aircrafts', viewsets.AircraftViewSet)
router.register(r'itineraries', viewsets.ItineraryViewSet)
router.register(r'travels', viewsets.TravelViewSet)
