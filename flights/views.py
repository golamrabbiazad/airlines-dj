from django.shortcuts import render
from .models import Flights


# Create your views here.


def index(req):
    return render(req, "flights/index.html", {
        "flights": Flights.objects.all()
    })


def flight(req, flight_id):
    flight = Flights.objects.get(pk=flight_id)
    return render(req, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all()
    })
