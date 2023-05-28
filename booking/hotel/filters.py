from django_filters import rest_framework as filters

from .models import Booked, Room


class AvailableRoomsFilter(filters.FilterSet):
    start_time = filters.DateTimeFilter(field_name='booked__start_time',
                                        lookup_expr='lte')
    end_time = filters.DateTimeFilter(field_name='booked__end_time',
                                      lookup_expr='gte')

    class Meta:
        model = Booked
        fields = ['start_time', 'end_time']


class RoomFilter(filters.FilterSet):
    cost = filters.NumberFilter(field_name='cost', lookup_expr='lte')
    count = filters.NumberFilter(field_name='count', lookup_expr='gte')

    class Meta:
        model = Room
        fields = ['cost', 'count']
