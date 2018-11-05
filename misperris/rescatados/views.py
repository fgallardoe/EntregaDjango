from django.shortcuts import render

from django.http import HttpResponse

from .models import Mascota

# Create your views here.
def index(request):
    latest_rescatados = Mascota.objects.order_by('-id_mascota')[:10]
    output = ", ".join(r.nom_mascota for r in latest_rescatados)
    return HttpResponse(output)



