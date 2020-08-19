from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flights, Passenger, Airport
# Create your views here.


def index(req):
    return render(req, "flights/index.html", {
        "flights": Flights.objects.all()
    })


def flight(req, flight_id):
    flight = Flights.objects.get(pk=flight_id)
    passengers = flight.passengers.all()
    return render(req, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers,
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })


def book(req, flight_id):
    if req.method == "POST":
        flight = Flights.objects.get(pk=flight_id)
        passenger_id = int(req.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
