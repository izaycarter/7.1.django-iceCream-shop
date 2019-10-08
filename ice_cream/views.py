from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Icecream

# Create your views here.
def title(request):

    topics = Icecream.objects.all()
    # ice_cream_list = Icecream.objects.filter()

    context = {
        "topics": topics
    }
    return render(request, "ice_cream/titles.html", context)




def flavors(request, title_id):

    flavor = get_object_or_404(Icecream, pk=title_id)
    context = {"flavor": flavor}
    return render(request, "ice_cream/flavors.html", context)
