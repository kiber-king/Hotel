from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Room(models.Model):
    number = models.IntegerField('Number of room', unique=True)
    cost = models.DecimalField('Price for room', max_digits=6,
                               decimal_places=2)
    count = models.PositiveIntegerField('Count')

    class Meta:
        ordering = ['-number']
        default_related_name = 'room'
        verbose_name = 'Room'


class Booked(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateField('Start')
    end_time = models.DateField('End')
