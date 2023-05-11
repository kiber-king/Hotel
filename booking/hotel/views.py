from rest_framework import generics, status
from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Room, Booked
from .serializers import RoomSerializer, BookedSerializer


class RoomList(APIView):
    def get(self, request):
        cost = self.request.query_params.get('cost', None)
        count = self.request.query_params.get('count', None)
        if cost:
            rooms = Room.objects.filter(cost__lte=cost)
        elif count:
            rooms = Room.objects.filter(count__gte=count)
        else:
            rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
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


class AvailableRoomList(generics.ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        start_time = self.request.query_params.get('start_time', None)
        end_time = self.request.query_params.get('end_time', None)
        if not start_time or not end_time:
            return Room.objects.none()
        bookings = Booked.objects.filter(start_time__lte=end_time,
                                         end_time__gte=start_time)
        booked_rooms = bookings.values_list('room', flat=True)
        available_rooms = Room.objects.exclude(id__in=booked_rooms)
        return available_rooms
