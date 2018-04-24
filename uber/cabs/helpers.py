from django.contrib.auth.models import User

from cabs.models import Driver, Passenger, TravelHistory


def create_user(validated_data):
    return User.objects.create_user(username=validated_data['username'],
                                    password=validated_data['password'],
                                    email=validated_data['email'],
                                    first_name=validated_data['first_name'],
                                    last_name=validated_data['last_name'])


def get_seats(preference, seats):
    rides_available = {'GO': 4, 'SUV': 6}
    if preference == 'POOL' and seats:
        return seats
    return rides_available[preference]


def find_cab(preference, seats):
    riders = get_seats(preference, seats)
    driver = Driver.objects.filter(seats_available=riders)
    if driver.exists():
        driver = driver.first()
        driver.seats_available -= riders
        driver.save()
        return driver
    else:
        return False


def active_user_rides(user):
    passenger = Passenger.objects.get(user=user)
    history = TravelHistory.objects.filter(passenger=passenger).last()
    if hasattr(history, 'status'):
        if getattr(history, 'status') == 'ACTIVE':
            return True
    return False
