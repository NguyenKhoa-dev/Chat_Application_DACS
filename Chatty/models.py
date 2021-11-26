from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.
class Information(models.Model):
    # Name = models.CharField(max_length=200)
    ImageLink = models.CharField(max_length=1000)
    Birthday = models.DateTimeField(auto_now_add=True)
    Status = models.BooleanField(default=False)
    UserName = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.UserName

class Room(models.Model):
    RoomName = models.CharField(max_length=300)
    Password = models.CharField(max_length=100)
    UserName = ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class Message(models.Model):
    Content = models.CharField(max_length=50000)
    RoomID = ForeignKey(Room, on_delete=models.CASCADE)