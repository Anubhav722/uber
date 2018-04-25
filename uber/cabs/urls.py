from django.conf.urls import url

from cabs.views import CabBooking, TravelHistoryView

urlpatterns = [
    url(r'^book/?$', CabBooking.as_view(), name='book'),
    url(r'^history/?$', TravelHistoryView.as_view(), name='history'),
]
