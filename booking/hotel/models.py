from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Room(models.Model):
    number = models.IntegerField()
    cost = models.FloatField()
    count = models.IntegerField()

    class Meta:
        ordering = ['-number']
        default_related_name = 'room'
        verbose_name = 'Комната'


class Booked(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateField('Start')
    end_time = models.DateField('End')

