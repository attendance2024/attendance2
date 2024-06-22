from django import forms
from django.contrib.auth.models import User
from .models import *

class  DateInput(forms.DateInput):
    input_type = 'date'

class studentform(forms.ModelForm):
    class Meta:
        model = student
        fields = '__all__'

        widgets = {
            'dob' : DateInput()
        }

        labels = {
            'reg_no' : "Registration Number",
            'dob' : "Date of birth",
            'contact_number' : "Contact Number",
            'program_id' : "Program ID",
            'dept' : "Department"
        }



