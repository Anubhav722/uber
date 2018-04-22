from rest_framework import viewsets

from cabs.models import Driver, Passenger, TravelHistory
from cabs.serializers import DriverSerializer, PassengerSerializer
# Create your views here.


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
