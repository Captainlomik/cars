from rest_framework import serializers

from .models import Person_auto, Dock
from django.contrib.auth.models import User


class PersonAutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person_auto
        fields = (
            'id',
            'name',
            'car_type',
            'price',
            'kilometrage',
            'gear_case',
            'color',
            'engine',
            'gear',
            'owner_count',
            'description'
        )

class DocksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Dock
        fields='__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="car:user-detail")
    class Meta:
        model = User
        fields = '__all__'
