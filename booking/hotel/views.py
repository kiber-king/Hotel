from rest_framework import generics, status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import filters, AvailableRoomsFilter, RoomFilter
from .models import Room, Booked
from .serializers import RoomSerializer, BookedSerializer


class RoomList(APIView):
    def get(self, request):
        queryset = Room.objects.all()
        filter = RoomFilter(request.GET, queryset=queryset)
        serializer = RoomSerializer(filter.qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


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
    queryset = Booked.objects.all()
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        try:
            booking = Booked.objects.get(id=self.kwargs['pk'])
            booking.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AvailableRoomsListAPIView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = AvailableRoomsFilter
