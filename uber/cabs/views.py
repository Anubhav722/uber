from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from cabs.models import Driver, Passenger, TravelHistory
from cabs.serializers import DriverSerializer, PassengerSerializer, TravelHistorySerializer
from cabs.permissions import IsDriver, IsPassenger
# Create your views here.


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = (IsDriver,)


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = (IsPassenger,)


class CabBooking(generics.GenericAPIView):
    queryset = TravelHistory.objects.all()
    serializer_class = TravelHistorySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            pass

    # def get(self, request, *args, **kwargs):
    #     import ipdb; ipdb.set_trace()
