from django.db import models
from index.models import User

# Create your models here.
class Event(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=500)
    recurring = models.BooleanField()
    date_type = models.CharField(max_length=20)
    message = models.CharField(max_length=500)
    created = models.DateTimeField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    last_send = models.DateTimeField(null=True)
    next_send = models.DateTimeField()
    interval = models.IntegerField(null=True)
    interval_type = models.CharField(max_length=50,null=True)
    snooze = models.NullBooleanField(null=True)
    snooze_interval = models.IntegerField(null=True)
    snooze_interval_type = models.CharField(max_length=50,null=True)
    snooze_last_send = models.DateTimeField(null=True)
    snooze_next_send = models.DateTimeField(null=True)
    warning = models.BooleanField()
    warning_interval = models.IntegerField(null=True)
    warning_interval_type = models.CharField(max_length=50)
    warning_next_send = models.DateTimeField()
    in_deleted = models.BooleanField()
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