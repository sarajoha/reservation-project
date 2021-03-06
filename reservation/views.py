from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm, get_dateForm
import quickstart
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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


@login_required
def reserve(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            start_datetime = post.start_datetime.isoformat()
            end_datetime = post.end_datetime.isoformat()
            full_name = ' '.join([post.user.first_name, post.user.last_name])
            quickstart.main(post.motive, full_name, post.user.first_name,
                            start_datetime, end_datetime)

            return redirect('reservations')
    else:
        form = ReservationForm()
    return render(request, 'reservation/reserve.html', {'form': form,})
