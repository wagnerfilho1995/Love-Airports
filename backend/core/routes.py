from rest_framework import routers, serializers, viewsets
from rest_framework.routers import DefaultRouter
from . import viewsets

'''
Setting Endpoints.
'''

router = DefaultRouter()

router.register(r'airport', viewsets.AirportViewSet)
