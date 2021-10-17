from django.db import models

# Create your models here.
class Airport(models.Model):
    class Meta:
        ordering = ['-id']
    iata = models.CharField(max_length=500, blank = False, null = False)
    city = models.CharField(max_length=500, blank = False, null = False)
    lat = models.FloatField(max_length=500, blank = False, null = False)
    lon = models.FloatField(max_length=500, blank = False, null = False)
    state = models.CharField(max_length=2, blank = False, null = False)

    def __str__(self):
        return self.iata

class Aircraft(models.Model):
    class Meta:
        ordering = ['-id']
    model = models.CharField(max_length=500, blank = False, null = False)
    manufacturer = models.CharField(max_length=500, blank = False, null = False)

    def __str__(self):
        return self.model

class Itinerary(models.Model):
    class Meta:
        ordering = ['-id']

    departure_time = models.DateTimeField(        
        auto_now = False, 
        auto_now_add = False,
        null = False,
        blank = False,
    )

    arrival_time = models.DateTimeField(        
        auto_now = False, 
        auto_now_add = False,
        null = False,
        blank = False,
    )

    fare_price = models.FloatField(max_length=500, blank = False, null = False)

    aircraft = models.ForeignKey(
        Aircraft, 
        on_delete = models.CASCADE,
        related_name='itinerary_aircraft',
        blank = False,
        null = False
    )

    def __str__(self):
        return self.departure_time.strftime("%m/%d/%Y, %H:%M:%S") + '->' + self.arrival_time.strftime("%m/%d/%Y, %H:%M:%S")

class Travel(models.Model):
    class Meta:
        ordering = ['-id']

    departure_date = models.DateField(        
        auto_now = False, 
        auto_now_add = False,
        null = False,
        blank = False,
    )

    origin = models.ForeignKey(
        Airport, 
        on_delete = models.CASCADE,
        related_name='travel_origin',
        blank = False,
        null = False
    )

    destination = models.ForeignKey(
        Airport, 
        on_delete = models.CASCADE,
        related_name='travel_destination',
        blank = False,
        null = False
    )

    currency = models.CharField(max_length=500, blank = False, null = False)

    itinerary = models.ForeignKey(
        Itinerary, 
        on_delete = models.CASCADE,
        blank = False,
        null = False
    )

    def __str__(self):
        return self.origin.state + '->' + self.destination.state