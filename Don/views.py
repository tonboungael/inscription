from django.shortcuts import render
from Admin.models import Don
from .table import DonateurForm
from Statistique.views import getStatistique

# Create your views here.


def suiviDon(request):
    #getStatistique()
    form = DonateurForm()
    return render(request,'don.html', {'form': form , 'dataDon':Don.objects.all()})

