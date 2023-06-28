from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import filters, AvailableRoomsFilter, RoomFilter
from .models import Room, Booked
from .serializers import RoomSerializer, BookedSerializer


class RoomList(APIView):
    def room_list(self, request):
        if request.method == 'POST':
            serializer = RoomSerializer(data=request.data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        rooms = Room.objects.all()
        filter = RoomFilter(request.GET, queryset=rooms)
        serializer = RoomSerializer(filter.qs, many=True)
        return Response(serializer.data)


class BookedList(generics.ListCreateAPIView):
    serializer_class = BookedSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        bookings = Booked.objects.filter(user=user)
        return bookings

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookedDelete(DestroyAPIView):
    serializer_class = BookedSerializer
    queryset = Booked.objects.all()
    permission_classes = [IsAuthenticated]
    obj = get_object_or_404(Booked, id=id)


class AvailableRoomsListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AvailableRoomsFilter
