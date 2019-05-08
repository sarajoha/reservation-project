from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm, get_dateForm
import quickstart

# Create your views here.
def reservations(request, date=None):

    if request.method == 'POST':
        date_form = get_dateForm(request.POST)
        if date_form.is_valid():
            start_date = date_form.data['start_date']
            end_date = date_form.data['end_date']
            reservation_list = Reservation.objects.filter(start_datetime__date__range=(start_date, end_date))
            return render(request, 'reservation/reservations.html', {'date_form':date_form,
                                                                    'reservation_list': reservation_list})
    else:
        date_form = get_dateForm()
        return render(request, 'reservation/reservations.html', {'date_form': date_form,})



def reserve(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            print(post)
            print(dir(post))
            print(post.motive, post.start_datetime, post.end_datetime)
            start_datetime = post.start_datetime.isoformat()
            end_datetime = post.end_datetime.isoformat()
            service = quickstart.main()
            event = {
                  'summary': post.motive,
                  'location': 'Sala de vidrio',
                  'start': {
                    'dateTime': start_datetime,
                    'timeZone': 'America/Bogota',
                  },
                  'end': {
                    'dateTime': end_datetime,
                    'timeZone': 'America/Bogota',
                  },
                }

            event = service.events().insert(calendarId='primary', body=event).execute()
            return redirect('reservations')
    else:
        form = ReservationForm()
    return render(request, 'reservation/reserve.html', {'form': form,})