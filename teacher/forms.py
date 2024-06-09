from django import forms
from .models import *

class editattendanceForm(forms.ModelForm):
    class Meta:
        model = editattendance
        fields = ['date', 'status']
