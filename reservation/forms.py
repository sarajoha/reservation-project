from django import forms
from .models import Reservation
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput
from django.utils import timezone



class ReservationForm(forms.ModelForm):

    #duration =

    class Meta:
        model = Reservation
        fields = ('start_datetime', 'duration', 'motive', 'user')
        labels = {'duration': 'Duracion', 'motive': 'Motivo', 'user': 'Usuario', 'start_datetime': 'Fecha y hora'}
        widgets = {
            'start_datetime': DateTimePickerInput(format='%Y-%m-%d %H:%M'),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_data = cleaned_data.get('start_datetime')
        duration = cleaned_data.get('duration')
        end_data = start_data + duration

        #qs1 = Reservation.objects.filter(Q(start_datetime__lte=end_data, end_datetime__gte=start_data) | Q(start_datetime__range=(start_data, end_data)) | Q(end_datetime__range=(start_data, end_data)))
        qs1 = Reservation.objects.filter(start_datetime__lte=end_data, end_datetime__gte=start_data)

        if start_data < timezone.now():
            raise forms.ValidationError('No puedes agendar una reunion para el pasado')

        elif qs1.exists():
            raise forms.ValidationError('Ya hay una reunion que empiza o termina en el momento seleccionado')


class get_dateForm(forms.Form):

    start_date = forms.DateField(label='Desde', widget=DatePickerInput(format='%Y-%m-%d'))
    end_date =  forms.DateField(label='Hasta', widget=DatePickerInput(format='%Y-%m-%d'))
