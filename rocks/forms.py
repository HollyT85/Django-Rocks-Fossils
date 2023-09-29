"""Imports for functionality"""
from django import forms
from .models import Rock

class RockForm(forms.ModelForm):

    class Meta:
        model = Rock
        fields = '__all__'