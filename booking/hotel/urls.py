from django.urls import path

from .views import RoomList, BookedList, BookedDelete

app_name = 'hotel'
urlpatterns = [
    path('roomlist/', RoomList.as_view()),
    path('booked/', BookedList.as_view()),
    path('booked/<int:pk>/delete/', BookedDelete.as_view()),

]
