from  django.forms import ModelForm
from django import forms

from Admin.models import Don


class DonateurForm(ModelForm):
    class Meta:
        model=Don
        fields=['montant']