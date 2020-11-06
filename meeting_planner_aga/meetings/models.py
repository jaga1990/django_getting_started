from datetime import time

from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=200)
    floor_number = models.IntegerField()
    room_number = models.FloatField()

    def __str__(self):
        return f"{self.name}: room {self.room_number} on {self.floor_number} floor"

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"



