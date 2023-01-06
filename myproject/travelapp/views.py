from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team


# Create your views here.
def first(request):
    obj1 = Place.objects.all()
    obj2 = Team.objects.all()
    return render(request, "index.html", {'result': obj1, 'answer': obj2})

