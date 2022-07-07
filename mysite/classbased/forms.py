#from dataclasses import fields
from .models import Laptops
from django import forms

class LaptopRegistration(forms.ModelForm):
    class Meta:
        model = Laptops
        fields = '__all__'