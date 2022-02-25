from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from .models import Pizza


# Create your views here.

def index(request):
    """pizzas = Pizza.objects.all()
    pizza_names_and_prices = [pizza.nom + " : " + str(pizza.prix)  for pizza in pizzas]
    pizza_name_str = ", ".join(pizza_names_and_prices)
    return HttpResponse("Nos pizzas: " + pizza_name_str)"""
    pizzas = Pizza.objects.all().order_by('prix')
    return render(request, 'menu/index.html', {'pizzas': pizzas})


def api_get_pizzas(request):
    pizzas = Pizza.objects.all().order_by('prix')
    json = serializers.serialize("json", pizzas)
    return HttpResponse(json)
