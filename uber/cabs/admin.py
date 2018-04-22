from django.contrib import admin

from cabs.models import Driver, Passenger, TravelHistory
# Register your models here.

admin.site.register(Driver)
admin.site.register(Passenger)
admin.site.register(TravelHistory)
