from django.db import models
from django import forms
from simpleduration import Duration, InvalidDuration
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
    '''
    Class describing an user that has 3 properties and 1 method:
        Properties:
        - first_name = First name of the User
        - last_name = Last name of the User
        - avatar = Avatar or image that represents the User
        Method:
        - __str__ = string representation of the object, returns
                    the first_name and the last_name as one string
    '''
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='avatars', blank=True)
    email = models.EmailField(max_length=255, blank=True, null=True, unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


    class Meta:
        ordering = ('first_name', )


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Reservation(models.Model):
    '''
    Class describing a reservation object that has 6 properties and 4 methods:
    Properties:
    - start_datetime = Date and time when the reservation starts
    - duration_text = Duration of the reservation, written as a number with a unit
    - duration = Duration of the reservations, corresponds to a timedelta type
    - end_datetime = Date and time when the reservation ends
    - motive = The reason of the reservation
    - user = User who is making the reservation, has to be a user object


    Method:
    - __str__ = string representation of the object, returns
                the motive and the start_datetime as one string in the form of
                'Hay motive el start_datetime'
    - calculate_duration = Transforms duration_text into a timedelta and saves it
                            in the duration field
    - calculate_time_end = Sums start_datetime and duration, saves the result into
                            the end_datetime property
    - save =
    '''
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

    class Meta:
        verbose_name = 'reservación 🤯'
        verbose_name_plural = 'reservaciones'
