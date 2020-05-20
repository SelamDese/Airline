from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Flight, Passenger

# Create your views here.
def index(request):
    # return HttpResponse("flights")
    context = {
        "flights" : Flight.objects.all()
    }
    return render(request, "flights/index.html", context)

def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")
    context = {
        "flight": flight,
        "passengers": flight.passengers.all()
     }
    return render(request, "flights/flight.html", context)

def Book(request, flight_id):
    try:
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        flight = Flight.objects.get(pk=flight_id)
    except KeyError:
    except Flight.DoesNotExist:
        return render(request, "flights/error.html", {"message":"No flight."})
    except Passenger.DoesNotExist:
        return render(request, "flights/error.html", {"message":"No passenger."})
