from django.db import models
# from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)
    user1 = models.CharField(max_length=100)
    user2 = models.CharField(max_length=1000)
    # user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room')
    # user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='room2')


class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=timezone.now, blank=True)
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100)
    # room = models.ForeignKey(Room, on_delete=models.CASCADE)