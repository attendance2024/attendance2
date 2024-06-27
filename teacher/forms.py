from django import forms
from .models import *
from student.models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm


class UserCreationFormExtended(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': 'username',
            'password1': 'password',
            'password2': 'confirm password',
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['reg_no', 'student_name', 'adm_no', 'email', 'year_of_adm', 'current_sem', 'contact_number', 'prg_id']
        labels = {
            'reg_no': 'registration number',
            'student_name': 'student name',
            'adm_no': 'admission number',
            'email': 'email',
            'year_of_adm': 'year of admission',
            'current_sem': 'current semester',
            'contact_number': 'contact number',
            'prg_id': 'program',
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['teacher_name', 'dept_id']
        labels = {
            'teacher_name': 'teacher name',
            'dept_id': 'department',
        }

class TeacherPositionForm(forms.Form):
    TEACHER_POSITIONS = [
        ('incharge', 'Incharge'),
        ('hod', 'HOD'),
        ('tutor', 'Tutor'),
        ('principal', 'Principal')
    ]
    teacher = forms.ModelChoiceField(queryset=teacher.objects.all(), required=True)
    position = forms.MultipleChoiceField(choices=TEACHER_POSITIONS, required=True, widget=forms.CheckboxSelectMultiple)
    dept_id = forms.ModelChoiceField(queryset=department.objects.all(), required=False)
    prg_id = forms.ModelChoiceField(queryset=programme.objects.all(), required=False)
    sem = forms.IntegerField(required=False)
    ex_id = forms.ModelChoiceField(queryset=extra_curricular_activities.objects.all(), required=False)

    def clean(self):
        cleaned_data = super().clean()
        position = cleaned_data.get("position")
        ex_id = cleaned_data.get("ex_id")

        if 'incharge' in position and not ex_id:
            self.add_error('ex_id', 'This field is required if the position is Incharge.')

        return cleaned_data

class EventForm(forms.ModelForm):
    class Meta:
        model = event
        fields = ['ex_id', 'event_description']
        labels = {
            'ex_id': 'extra-curricular activity',
            'event_description': 'event description',
        }
