from django.contrib.auth.models import User

from rest_framework import serializers
# from rest_framework.validators import UniqueValidator

from cabs.models import Driver, Passenger, TravelHistory
from cabs.helpers import create_user


class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email', 'username', 'password')


class DriverSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    capacity = serializers.IntegerField(min_value=1, max_value=6)
    seats_available = serializers.IntegerField(min_value=1, max_value=6)

    class Meta:
        model = Driver
        fields = ('id', 'user',
                  'cab_no', 'seats_available',
                  'capacity', 'contact_no')

    def create(self, validated_data):
      user = create_user(validated_data.pop('user'))
      return Driver.objects.create(user=user, **validated_data)


class PassengerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Passenger
        fields = ('id', 'user',
                  'contact_no')

    def create(self, validated_data):
      user = create_user(validated_data.pop('user'))
      return Passenger.objects.create(user=user, **validated_data)


class TravelHistorySerializer(serializers.ModelSerializer):
    choices = ['GO', 'POOL', 'SUV']
    seats_requested = serializers.IntegerField(min_value=1, max_value=6, required=False)
    preference = serializers.ChoiceField(choices)

    class Meta:
        model = TravelHistory
        fields = ('id', 'seats_requested',
                  'pickup_location',
                  'drop_location',
                  'preference')

    # def get_preference(self, obj):
    #   return obj.get_preference_display()
