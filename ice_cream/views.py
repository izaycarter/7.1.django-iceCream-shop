from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import IceCream

# Create your views here.
def index(request, selection=None):

    if selection == "home":
        ice_cream_list = IceCream.objects.all()
    elif selection == 'featured':
        ice_cream_list = IceCream.objects.filter(featured=True)
    else:
        ice_cream_list = IceCream.objects.filter(available=selection.upper())

    context = {
        "ice_cream_list": ice_cream_list
    }

    return render(request, "ice_cream/index.html", context)
