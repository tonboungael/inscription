from  django.forms import ModelForm
from django import forms
from .models import Hopital


class DonateurForm(ModelForm):
    class Meta:
        model=Hopital
        fields=['nomH', 'adresse','num_compte']