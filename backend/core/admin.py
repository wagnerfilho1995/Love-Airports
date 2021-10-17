from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Airport)
admin.site.register(Aircraft)
admin.site.register(Itinerary)
admin.site.register(Travel)