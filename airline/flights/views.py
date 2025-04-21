from django.shortcuts import render, redirect
from .models import Flight, Passenger

# Create your views here.

def index(request):
    ctx = {'flights': Flight.objects.all()}
    return render(request, 'flights/index.html', ctx)

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    passengers = flight.passengers.all()
    ctx = {'flight': flight, 'passengers':passengers, 'non_passengers': Passenger.objects.exclude(flights=flight)}
    return render(request, 'flights/flight.html', ctx)


def book(request, flight_id):
    if request.method == 'POST':
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST['passenger']))
        passenger.flights.add(flight)
        return redirect('flight', flight_id)
    