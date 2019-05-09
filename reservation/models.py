from django.db import models
from django import forms
from simpleduration import Duration, InvalidDuration


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Reservation(models.Model):
    STANDUP = 'SU'
    CLASS = 'CL'
    MOTIVE_CHOICES = ((STANDUP, 'Stand Up'), (CLASS, 'Clase'), )

    start_datetime = models.DateTimeField(null=True)
    duration_text = models.CharField(max_length=100, null=True, blank=True)
    duration = models.DurationField(blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)
    motive = models.CharField(max_length=20, choices=MOTIVE_CHOICES) #which choices?
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def calculate_duration(self):
        try:
            dur = Duration(self.duration_text)
            dur_td = dur.timedelta()
            self.duration = dur_td
        except InvalidDuration:
            pass


    def calculate_time_end(self):
        self.end_datetime = self.start_datetime + self.duration


    def save(self, *args, **kwargs):
        self.calculate_duration()
        self.calculate_time_end()
        super().save(*args, **kwargs)


    def __str__(self):
        return f'Hay {self.motive} el {self.start_datetime}'
