from django.shortcuts import render
from .form import DonateurForm
from .models import Hopital
from Statistique.models import Gouvernorat

# Create your views here.

def formHospital(request):
    if request.method == "POST":
        name = request.POST.get("nomH")
        adress = request.POST.get("adresse")
        num = request.POST.get("num_compte")
        gouv = request.POST.get("gouvernorat_FK")
        Hopital.objects.create(nomH=name,adresse=adress,num_compte=num,gouvernorat_FK=gouv)
        return redirect('administrateur/')
def index(request):
    form = DonateurForm()
    return render(request,'index.html',{'gouv':Gouvernorat.objects.all()})
