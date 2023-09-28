"""Imports for functionality"""
from django import forms
from .models import Rock

class RockForm(forms.ModelForm):

    class Meta:
        model = Rock
        # fields = [
        #     'owner', 'title', 'extra_info', 'location',
        #     'material', 'size', 'era', 'tools_used', 
        #     'date_found', 'prepped_self', 'image'
        # ]
        fields = '__all__'