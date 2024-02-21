from django import forms
from .models import *

class studentform(forms.ModelForm):
    class Meta:
        model = department
        fields = '__all__'
