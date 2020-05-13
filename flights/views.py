from django.http import HttpResponse
from django.shortcuts import render
from .models import Flight

# Create your views here.
def index(request):
    # return HttpResponse("flights")
    context = {
        "flights" : Flight.object.all()
    }
    return render(request, "flights/index.html", contaxt)
