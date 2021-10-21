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
from conf.permissions import api_username, api_pass, api_key
from .utils import *
import random
from django.utils import timezone
from django.db.models import Count
from datetime import date, datetime, timedelta

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
            Essa função percorre uma lista com todos os aeroportos da API mockup de aeroportos domésticos 
            e cria um Airport no banco de dados em cada iteração
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

    @action(detail=False,  methods=['get'])
    def airports_X_airports(self, request, pk=None):
        '''
            Essa função faz 20x20 combinações entre aeroportos diferentes, salvando cada viagem
            entre eles, calculando e retornando a melhor opção de voo a ser tomado para cada uma 
            delas.
        '''

        random_airports = AirportSerializer(Airport.objects.order_by('?')[:40], many=True)
        
        # 40 dias a frente de hoje
        date = (datetime.today() + timedelta(days = 40)).strftime('%Y-%m-%d')
        combinations = []
        for airport_1 in random_airports.data[:20]:
            suitable = {}
            for airport_2 in random_airports.data[20:]:
                url = f'http://stub.2xt.com.br/air/search/{api_key}/{airport_1["iata"]}/{airport_2["iata"]}/{date}'
                response = requests.get(url,
                            auth = (api_username, api_pass))
                dist = round(haversine(airport_1['lat'], airport_1['lon'], airport_2['lat'], airport_2['lon']), 2)
                suitable['cost'] = -1
                departure_date = datetime.strptime(response.json()['summary']['departure_date'], '%Y-%m-%d')
                currency = response.json()['summary']['currency']
                for data in response.json()['options']:
                    try:
                        aircraft, created = Aircraft.objects.get_or_create(
                            model=data['aircraft']['model'],
                            manufacturer=data['aircraft']['manufacturer']
                        )
                    except:
                        Response({'erro', 'Erro ao criar avião'}, status=status.HTTP_400_BAD_REQUEST)

                    
                    departure_time = datetime.strptime(data['departure_time'], '%Y-%m-%dT%H:%M:%S')
                    arrival_time = datetime.strptime(data['arrival_time'], '%Y-%m-%dT%H:%M:%S')
                    time_delta = (arrival_time - departure_time)
                    hours = (time_delta.total_seconds() / 60) / 60
                    if suitable['cost'] == -1:
                        suitable['cost'] = float(data['fare_price'])
                        suitable['dist'] = dist
                        suitable['url'] = url
                        suitable['aircraft'] = aircraft
                    elif suitable['cost'] > float(data['fare_price']):
                        suitable['cost'] = float(data['fare_price'])
                        suitable['dist'] = dist
                        suitable['url'] = url
                        suitable['aircraft'] = aircraft

                    try:
                        itinerary, created_itinerary = Itinerary.objects.get_or_create(
                            departure_time=departure_time,
                            arrival_time=arrival_time,
                            fare_price=float(data['fare_price']),
                            aircraft=aircraft
                        )
                    except:
                        Response({'erro', 'Erro ao criar itinerário'}, status=status.HTTP_400_BAD_REQUEST)

                    if hours < 1:
                        velocity_km = (dist/int(hours * 100)/100)
                    else: 
                        velocity_km = dist/int(hours)
                    
                    duration_h = round(hours, 2)
                    fare_by_km = round(float(data['fare_price'])/int(dist), 2)
                    velocity_km = round(velocity_km, 2)

                    try:
                        travel = Travel.objects.create(
                            departure_date=departure_date,
                            origin=Airport.objects.get(id=airport_1['id']),
                            destination=Airport.objects.get(id=airport_2['id']),
                            currency=currency,
                            duration_h=duration_h,
                            velocity_km=velocity_km,
                            fare_by_km=fare_by_km,
                            itinerary=itinerary
                        )
                    except:
                        Response({'erro', 'Erro ao criar objeto Travel'}, status=status.HTTP_400_BAD_REQUEST)


            if suitable['url']:
                try:
                    suitable, created = Suitable.objects.get_or_create(
                        url=suitable['url'],
                        dist=suitable['dist'],
                        cost=suitable['cost'],
                        aircraft=suitable['aircraft']
                    )
                except:
                    Response({'erro', 'Erro ao criar objeto Suitable'}, status=status.HTTP_400_BAD_REQUEST)
                combinations.append(suitable)

        return Response(combinations)

    @action(detail=False,  methods=['get'])
    def get_airports_demography(self, request, pk=None):
        airports = Airport.objects.values('state').annotate(Count('id')).order_by().filter(id__count__gt=0)
        resp = {}
        for airports in airports:
            resp[airports['state']] = airports['id__count']
        
        return Response(dict(sorted(resp.items(), key=lambda item: item[1], reverse=True)))
    
    @action(detail=False,  methods=['get'])
    def get_airports_distance(self, request, pk=None):
        
        airports = AirportSerializer(Airport.objects.all(), many=True)
        resp = {}

        for airport1 in airports.data:
            for airport2 in airports.data:
                if airport1['id'] != airport2['id']:
                    dist = haversine(airport1['lat'], airport1['lon'], airport2['lat'], airport2['lon'])
                    if airport1['iata'] not in resp:
                        resp[airport1['iata']] = {
                            'iata': airport1['iata'],
                            'closer': {
                                'dist': dist,
                                'iata': airport2['iata']
                            },
                            'faraway':  {
                                'dist': dist,
                                'iata': airport2['iata']
                            }
                        }
                    else:  
                        if dist < resp[airport1['iata']]['closer']['dist']:
                            resp[airport1['iata']]['closer']['dist'] = dist
                            resp[airport1['iata']]['closer']['iata'] = airport2['iata']
                        elif resp[airport1['iata']]['faraway']['dist'] < dist:
                            resp[airport1['iata']]['faraway']['dist'] = dist    
                            resp[airport1['iata']]['faraway']['iata'] = airport2['iata']                  
        
        return Response(resp)

class AircraftViewSet(viewsets.ModelViewSet):
    
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    permission_classes = [permissions.AllowAny]
    
    http_method_names = ['get', 'post', 'options', 'head', 'put', 'update', 'delete']

class ItineraryViewSet(viewsets.ModelViewSet):
    
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer
    permission_classes = [permissions.AllowAny]
    
    http_method_names = ['get', 'post', 'options', 'head', 'put', 'update', 'delete']

class TravelViewSet(viewsets.ModelViewSet):
    
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [permissions.AllowAny]
    
    http_method_names = ['get', 'post', 'options', 'head', 'put', 'update', 'delete']

    @action(detail=False,  methods=['get'])
    def long_trips(self, request, pk=None):
        #models = TravelSerializer(Travel.objects.filter()[:30].order_by('duration_h'), many=True)
        models = Travel.objects.filter(duration_h__isnull=False).order_by('-duration_h')[:30]
        models = TravelSerializer(models, many=True)
        
        return Response(models.data)

class SuitableViewSet(viewsets.ModelViewSet):
    
    queryset = Suitable.objects.all()
    serializer_class = SuitableSerializer
    permission_classes = [permissions.AllowAny]
    
    http_method_names = ['get', 'post', 'options', 'head', 'put', 'update', 'delete']