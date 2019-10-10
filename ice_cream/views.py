from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import IceCream
from django.urls import reverse, reverse_lazy
from django.views import generic

# Create your views here.
def index(request, selection=None):

    if selection == "home":
        ice_cream_list = IceCream.objects.all()
    elif selection == 'featured':
        ice_cream_list = IceCream.objects.filter(featured=True)
    elif selection != None:
        ice_cream_list = IceCream.objects.filter(available=selection.upper())
    else:
        ice_cream_list = IceCream.objects.all()

    context = {
        "ice_cream_list": ice_cream_list
    }

    return render(request, "ice_cream/index.html", context)


class ResultsView(generic.DetailView):
    model = IceCream
    template_name ="ice_cream/results.html"

def vote(request, pk):

    ice_cream = get_object_or_404(IceCream, pk=pk)
    # e.g. {'flavor': 'vanilla', 'available': 'weekly', 'featured': True, likes: 0}

    ice_cream.likes += 1
    ice_cream.save()

    return HttpResponseRedirect(reverse('ice_cream:results', args=(ice_cream.id,)))


class CreateIceCream(generic.CreateView):

    model = IceCream
    # fields = '__all__'
    fields = ["flavor","base","available","featured","date_churned",]
    template_name = "ice_cream/create.html"

class DeleteIceCream(generic.DeleteView):
    model = IceCream
    success_url = reverse_lazy("ice_cream:index")
