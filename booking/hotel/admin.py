from django.contrib import admin

from .models import Room, Booked


class AdminRoom(admin.ModelAdmin):
    list_display = ('number', 'cost', 'count')
    search_fields = ('number', 'cost', 'count')


admin.site.register(Room, AdminRoom)


class AdminBooked(admin.ModelAdmin):
    list_display = ('room', 'start_time', 'end_time')
    search_fields = ('room', 'start_time', 'end_time')


admin.site.register(Booked, AdminBooked)
