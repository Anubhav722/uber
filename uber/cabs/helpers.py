from django.contrib.auth.models import User


def create_user(validated_data):
    return User.objects.create_user(username=validated_data['username'],
                                    password=validated_data['password'],
                                    email=validated_data['email'],
                                    first_name=validated_data['first_name'],
                                    last_name=validated_data['last_name'])
