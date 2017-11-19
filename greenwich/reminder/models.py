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
    last_send = models.DateTimeField()
    next_send = models.DateTimeField()
    interval = models.IntegerField()
    interval_type = models.CharField(max_length=50)
    snooze = models.BooleanField()
    snooze_interval = models.IntegerField()
    snooze_interval_type = models.CharField(max_length=50)
    snooze_last_send = models.DateTimeField()
    snooze_next_send = models.DateTimeField()
    warning = models.BooleanField()
    warning_interval = models.IntegerField()
    warning_interval_type = models.CharField(max_length=50)
    warning_next_send = models.DateTimeField()
    in_deleted = models.BooleanField()