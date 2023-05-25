from django.contrib import admin

from .models import Room, Booked


@admin.register(Room)
class AdminRoom(admin.ModelAdmin):
    list_display = ('number', 'cost', 'count')
    search_fields = ('number', 'cost', 'count')


@admin.register(Booked)
class AdminBooked(admin.ModelAdmin):
    list_display = ('room', 'start_time', 'end_time')
    search_fields = ('room', 'start_time', 'end_time')
