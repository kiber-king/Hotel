from rest_framework import serializers

from .models import Room, Booked


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class BookedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booked
        fields = '__all__'
