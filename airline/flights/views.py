from django.shortcuts import render
from .models import Flight

# Create your views here.

def index(request):
    ctx = {'flights': Flight.objects.all()}
    return render(request, 'flights/index.html', ctx)

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    passengers = flight.passengers.all()
    ctx = {'flight': flight, 'passengers':passengers}
    return render(request, 'flights/flight.html', ctx)
