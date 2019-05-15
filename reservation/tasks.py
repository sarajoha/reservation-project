#Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import Reservation, User
from django.utils import timezone


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)

#periodic task to be run every monday morning with celery beats
def user_with_most_reservations():
    last_week = timezone.now() - timezone.timedelta(weeks=1)
    yesterday = timezone.now() - timezone.timedelta(days=1)

    #user that made more reservations last week
    user = User.objects.distinct().filter(reservation__start_datetime__range=(last_week, yesterday)).annotate(count=Count('reservation')).order_by('-count').first()
    return user.get_full_name()
