from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

from core.models import BaseModel

# Third party imports
from model_utils import Choices
# Create your models here.


class Driver(BaseModel):
    user = models.ForeignKey(User, related_name='driver')
    cab_no = models.CharField(max_length=10)
    seats_available = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    contact_no = models.CharField(max_length=12)

    def __unicode__(self):
        return self.user.username


class Passenger(BaseModel):
    user = models.ForeignKey(User, related_name='passenger')
    contact_no = models.CharField(max_length=12)

    def __unicode__(self):
        return self.user.username


class TravelHistory(BaseModel):
    PREFERENCE_TYPE = Choices('GO', 'POOL', 'SUV')

    driver = models.ForeignKey(Driver)
    passenger = models.ForeignKey(Passenger)
    pickup_location = models.CharField(max_length=40)
    drop_location = models.CharField(max_length=40)
    seats_requested = models.PositiveIntegerField()
    preference = models.CharField(max_length=4,
                                  choices=PREFERENCE_TYPE,
                                  default=PREFERENCE_TYPE.GO)

    def __unicode__(self):
        return (self.pickup_location + " --> " + self.drop_location)


# This receiver handles token creation immediately a new user is created.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
