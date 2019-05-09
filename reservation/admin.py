from django.contrib import admin
from .models import User, Reservation
from django.contrib.humanize.templatetags.humanize import naturalday
from django.utils import timezone
from django.utils.html import format_html
from django.http import HttpResponse
import tablib

def print_to_console(modeladmin, request, queryset):
    print(queryset)

def export_as_excel(modeladmin, request, queryset):
    headers = ('fecha', 'duracion', 'usuario', 'motivo', )

    data_array = []
    for q in queryset:
        data_array.append((str(q.start_datetime), str(q.duration), q.user.first_name, q.get_motive_display(), ))

    data = tablib.Dataset(*data_array, headers=headers)
    response = HttpResponse(data.export('xlsx'), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    # response = HttpResponse(data.export('json'), content_type='application/json')
    return response

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('start_datetime', 'duration', 'end_datetime', 'motive',
    'user', 'image_tag', 'hora_humanizada', 'en_el_futuro',  )
    list_filter = ('user', 'start_datetime', )
    search_fields = ('user__first_name', 'user__last_name', )
    date_hierarchy = 'start_datetime'
    actions = (print_to_console, export_as_excel, )

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
            # return format_html('<img src="{}" />'.format(obj.user.avatar.url))
            return format_html('<img src="{}" />'.format(obj.user.avatar.url))
        else:
            return None

    en_el_futuro.boolean = True
    image_tag.short_description = 'User image'


# Register your models here.
admin.site.register(User)
admin.site.register(Reservation, ReservationAdmin)
