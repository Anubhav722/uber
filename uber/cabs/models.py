from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from core.models import BaseModel

# Create your models here.


class Driver(BaseModel):
    user = models.ForeignKey(User, related_name='driver')
    cab_no = models.CharField(max_length=8)
    seats_available = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    location = models.CharField(max_length=40)

    def __unicode__(self):
        return self.user.username


class Passenger(BaseModel):
    user = models.ForeignKey(User, related_name='passenger')
    contact_no = models.CharField(max_length=12)
    location = models.CharField(max_length=40)

    def __unicode__(self):
        return self.user.username


class TravelHistory(BaseModel):
    driver = models.ForeignKey(Driver)
    passenger = models.ForeignKey(Passenger)
    pickup_location = models.CharField(max_length=40)
    drop_location = models.CharField(max_length=40)
    seats_requested = models.PositiveIntegerField()

    def __unicode__(self):
        return (self.pickup_location + " --> " + self.drop_location)
