from django.conf.urls import url

from cabs.views import CabBooking

urlpatterns = [
    url(r'^book/?$', CabBooking.as_view(), name='book'),
    # url(r'^history/?$', RideHistory.as_view(), name='history')
]
