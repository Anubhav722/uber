# from rest_framework import viewsets
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cabs.models import Driver, Passenger, TravelHistory
from cabs.serializers import DriverSerializer, PassengerSerializer, TravelHistorySerializer
from cabs.permissions import IsDriver, IsPassenger
from cabs.helpers import find_cab, active_user_rides, get_seats
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
            if not request.user.username:
                return Response(
                    {'status': 'Failed',
                     'details': 'Authentication credentials not provided'},
                    status=status.HTTP_403_FORBIDDEN)
            if Passenger.objects.filter(user=request.user).exists():
                if active_user_rides(request.user):
                    return Response(
                        {'status': 'Failed',
                         'details': 'You currently have an active ride'},
                        status=status.HTTP_400_BAD_REQUEST)
                preference = serializer.validated_data.get('preference')
                seats = serializer.validated_data.get('seats_requested')
                if preference == 'POOL' and not seats:
                    return Response(
                        {'status': 'Failed',
                         'details': 'Please provide seats when \
                                     looking to pool'},
                        status=status.HTTP_400_BAD_REQUEST)
                driver = find_cab(preference, seats)
                if driver:
                    seats = get_seats(preference, seats)
                    passenger = Passenger.objects.get(user=request.user)
                    TravelHistory.objects.create(driver=driver,
                                                 passenger=passenger,
                                                 pickup_location=serializer.data.get('pickup_location'),
                                                 drop_location=serializer.data.get('drop_location'),
                                                 preference=preference,
                                                 seats_requested=seats,
                                                 status='ACTIVE')
                    return Response(
                        {'status': 'Success',
                         'details': 'Driver Name: {} \
                                     Cab No.: {} \
                                     Contact No.: {}'.format(
                                    driver.user.username,
                                    driver.cab_no,
                                    driver.contact_no)},
                        status=status.HTTP_201_CREATED)
                else:
                    return Response(
                        {'status': 'Failed',
                         'details': 'Sorry currently no ride is available'},
                        status=status.HTTP_200_OK)
            else:
                return Response(
                    {'status': 'Failed',
                     'details': 'Unauthenticated User'},
                    status=status.HTTP_403_FORBIDDEN)
        else:
            return serializer.errors

    def put(self, request, *args, **kwargs):
        # import ipdb; ipdb.set_trace()
        print self.request
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not request.user.username:
                return Response(
                    {'status': 'Failed',
                     'details': 'Authentication credentials not provided'},
                    status=status.HTTP_403_FORBIDDEN)
            driver = Driver.objects.filter(user=request.user)
            if driver.exists():
                # import ipdb; ipdb.set_trace()
                history = TravelHistory.objects.filter(driver=driver).last()
                if history:
                    if history.status == 'ACTIVE':
                        history.status = 'FINISHED'
                        history.save()
                        return Response(
                            {'status': 'Success',
                             'details': 'Ended trip successfully'},
                            status=status.HTTP_200_OK)
                return Response(
                    {'status': 'Failed',
                     'details': 'You have no active rides'},
                    status=status.HTTP_200_OK)
            else:
                return Response(
                    {'status': 'Failed',
                     'details': 'Authentication credentials not provided'},
                    status=status.HTTP_403_FORBIDDEN)

        else:
            # import ipdb; ipdb.set_trace()
            return Response(
                {'status': 'Failed',
                 'details': serializer.errors},
                status=status.HTTP_403_FORBIDDEN)
            # return serializer.errors


# class EndTrip(generics.GenericAPIView):
#     queryset = TravelHistory.objects.all()
#     serializer_class = 
