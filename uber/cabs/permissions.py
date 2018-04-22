from rest_framework.permissions import BasePermission
from cabs.models import Driver, Passenger


class IsDriver(BasePermission):

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Driver):
            return obj.user == request.user

        return obj.user == request.user


class IsPassenger(BasePermission):

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Passenger):
            return obj.user == request.user
        return obj.user == request.user
