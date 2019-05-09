from django.contrib import admin
from .models import User, Reservation
from django.contrib.humanize.templatetags.humanize import naturalday
from django.utils import timezone
from django.utils.html import format_html


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('start_datetime', 'duration', 'end_datetime', 'motive',
    'user', 'image_tag', 'hora_humanizada', 'en_el_futuro',  )

    ordering = ('-start_datetime', )

    def hora_humanizada(self, obj):
        return naturalday(obj.start_datetime)

    def en_el_futuro(self, obj):
        if obj.start_datetime > timezone.now():
            return True
        else:
            return False

    def image_tag(self, obj):
        if obj.user.avatar:
            return format_html('<img src="{}" />'.format(obj.user.avatar.url))
        else:
            return None

    en_el_futuro.boolean = True
    image_tag.short_description = 'User image'

# Register your models here.
admin.site.register(User)
admin.site.register(Reservation, ReservationAdmin)
