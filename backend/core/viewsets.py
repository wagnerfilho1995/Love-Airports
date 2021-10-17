from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .serializers import *
from .models import *
import requests
from requests.auth import HTTPBasicAuth
from conf.permissions import api_username, api_pass

'''
As classes desse arquivo realizam uma query (queryset = Model.objects.all()) dos Models e retornam essa requisição para o usuário
no formato serializado (serializer_class = ModelSerializer) definido em ./serializers.py.
'''

class AirportViewSet(viewsets.ModelViewSet):
    
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    permission_classes = [permissions.AllowAny]
    
    http_method_names = ['get', 'post', 'options', 'head', 'put', 'update', 'delete']

    @action(detail=False,  methods=['get'])
    def get_all_airports(self, request, pk=None):
        '''
            Essa função retorna uma lista com todos os aeroportos da API mockup de aeroportos domésticos
        '''

        # Request get da api passando login e senha
        response = requests.get('http://stub.2xt.com.br/air/airports/ruGvDHwlzwbbujWq9DrOvJd3mzcvOWvj',
                    auth = (api_username, api_pass))

        return Response(response.json())
    
    @action(detail=False,  methods=['get'])
    def build_airports_database(self, request, pk=None):
        '''
            Essa função retorna uma lista com todos os aeroportos da API mockup de aeroportos domésticos
        '''

        # Request get da api passando login e senha
        response = requests.get('http://stub.2xt.com.br/air/airports/ruGvDHwlzwbbujWq9DrOvJd3mzcvOWvj',
                    auth = (api_username, api_pass))
                    
        for iata, data in response.json().items():
            try:
                airport, created = Airport.objects.get_or_create(
                    iata=iata,
                    city=data['city'],
                    lat=float(data['lat']),
                    lon=float(data['lon']),
                    state=data['state']
                )
            except:
                Response({'erro', 'Erro ao criar aeroporto'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(response.json())