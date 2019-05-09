from django import forms
from .models import Reservation
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput
from django.utils import timezone
from simpleduration import Duration, InvalidDuration



class ReservationForm(forms.ModelForm):

    #duration =

    class Meta:
        model = Reservation
        fields = ('start_datetime', 'duration_text', 'motive', 'user')
        labels = {'duration_text': 'Duracion', 'motive': 'Motivo', 'user': 'Usuario', 'start_datetime': 'Fecha y hora'}
        widgets = {
            'start_datetime': DateTimePickerInput(format='%Y-%m-%d %H:%M'),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_data = cleaned_data.get('start_datetime')
        duration_text = cleaned_data.get('duration_text')
        duration_worked = False

        try:
            dur = Duration(duration_text)
            dur_td = dur.timedelta()
            duration = dur_td
            end_data = start_data + duration
            qs1 = Reservation.objects.filter(start_datetime__lte=end_data, end_datetime__gte=start_data)
            duration_worked = True
        except InvalidDuration:
            pass

        if duration_worked == False:
            raise forms.ValidationError('Esta duracion no es valida')

        elif start_data < timezone.now():
            raise forms.ValidationError('No puedes agendar una reunion para el pasado')

        elif qs1.exists():
            raise forms.ValidationError('Ya hay una reunion que empiza o termina en el momento seleccionado')


class get_dateForm(forms.Form):

    start_date = forms.DateField(label='Desde', widget=DatePickerInput(format='%Y-%m-%d'))
    end_date =  forms.DateField(label='Hasta', widget=DatePickerInput(format='%Y-%m-%d'))
