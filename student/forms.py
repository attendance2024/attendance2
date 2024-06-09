from django import forms
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


class teacherform(forms.ModelForm):
    class Meta:
        model = teacher
        fields = '__all__'

class tutorform(forms.ModelForm):
    class Meta:
        model = tutor
        fields = '__all__'

class hodform(forms.ModelForm):
    class Meta:
        model = hod
        fields = '__all__'

class addform(forms.ModelForm):
    class Meta:
        model = addattendance
        fields = '__all__'    
        
    
