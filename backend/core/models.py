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