"""Imports for functionality"""
from django.forms import TextInput
from django import forms
from .models import Rock

class RockForm(forms.ModelForm):
    class Meta:
        model = Rock
        exclude = ['user',]
        widgets = {
            'date_found': forms.DateInput(attrs={'type': 'date'}),
            'owner': TextInput(attrs={'readonly': 'readonly'})
        }