from django import forms
from .models import *
from student.models import *




class EventForm(forms.ModelForm):
    class Meta:
        model = event
        fields = ['ex_id', 'event_description']