from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models


# Create your models here.


class User(AbstractUser):
    profile_picture = models.CharField(max_length=250, blank=True, null=True)
    last_seen = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    request = models.ForeignKey('Request', on_delete=models.CASCADE, null=True, blank=True)
    notification = models.ForeignKey('Notification', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.get_full_name()


class Request(models.Model):
    initiator_username = models.CharField(max_length=250, blank=False)
    recipient_username = models.CharField(max_length=250, blank=False)
    REQUEST_STATUS = [
        ('P', 'PENDING'),
        ('D', 'DECLINED'),
        ('A', 'ACCEPTED'),
    ]
    status = models.CharField(max_length=8, choices=REQUEST_STATUS)
    REQUEST_TYPE = [
        ('FR', 'FRIEND_REQUEST'),
        ('GIR', 'GROUP_INVITE_REQUEST'),
    ]
    type = models.CharField(max_length=20, choices=REQUEST_TYPE)
    time_initiated = models.DateTimeField(auto_now_add=True)
    time_accepted_or_declined = models.DateTimeField(blank=True, null=True, max_length=10)


class Notification(models.Model):
    request = models.ForeignKey(Request, on_delete=models.PROTECT)
    recipient_username = models.CharField(max_length=250, blank=False)


class Chat(models.Model):
    sender_username = models.CharField(max_length=250, blank=False)
    recipient_username = models.CharField(max_length=250, blank=False)
    message = models.CharField(max_length=1000, blank=False)
    time_created = models.DateTimeField(auto_now_add=True)
