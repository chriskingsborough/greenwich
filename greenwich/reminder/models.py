from django.db import models
from index.models import User
# Create your models here.


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=500)
    recurring = models.BooleanField(default=True)
    message = models.CharField(max_length=500)
    created = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    last_send = models.DateTimeField(null=True)
    next_send = models.DateTimeField()
    interval = models.IntegerField(null=True, default=1)
    interval_type = models.CharField(max_length=50, null=True, default='week(s)')
    snooze = models.NullBooleanField(null=True)
    snooze_interval = models.IntegerField(null=True)
    snooze_interval_type = models.CharField(max_length=50, null=True)
    snooze_last_send = models.DateTimeField(null=True)
    snooze_next_send = models.DateTimeField(null=True)
    warning = models.BooleanField(default=True)
    warning_interval = models.IntegerField(null=True, default=1)
    warning_interval_type = models.CharField(max_length=50, default='day(s)')
    warning_next_send = models.DateTimeField()
    in_deleted = models.BooleanField(default=False)
    interval_type.choices = (
        ('day', 'day(s)'),
        ('week', 'week(s)'),
        ('month', 'month(s)'),
        ('year', 'year(s)')
    )
    warning_interval_type.choices = (
        ('day', 'day(s)'),
        ('week', 'week(s)'),
        ('month', 'month(s)'),
        ('year', 'year(s)')
    )


class MessageLog(models.Model):
    users_id = models.IntegerField(null=True)
    event_id = models.IntegerField(null=True)
    sent = models.DateTimeField(null=True)
    phone_number = models.CharField(max_length=50)