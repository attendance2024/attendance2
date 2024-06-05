from django.db import models
from django.conf import settings
from django import forms
# Create your models here.
class department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=120)
    sem = models.IntegerField()
    graduation = models.CharField(max_length=120)
    
    def __str__(self):
        return self.dept_name

class student(models.Model):
    student_ID = models.AutoField(primary_key=True)
    reg_no = models.CharField(max_length=10)
    name = models.CharField(max_length=120)
    dob = models.DateField()
    email = models.EmailField()
    contact_number = models.CharField(max_length=10)
    program_id = models.IntegerField()
    dept = models.ForeignKey(department,on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    contact_number = models.CharField(max_length=10)
    dept = models.ForeignKey(department,on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
class tutor(models.Model):
    tutor_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=120)
    email = models.EmailField()
    contact_number = models.CharField(max_length=10)
    dept = models.ForeignKey(department,on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
class hod(models.Model):
    hod_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    contact_number = models.CharField(max_length=10)
    dept = models.ForeignKey(department,on_delete=models.CASCADE)  
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=120)
    event_date = models.DateField()
    hour_attended = models.IntegerField()
    dept = models.ForeignKey(department,on_delete=models.CASCADE)

class addattendance(models.Model):
    student_name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=20)
    roll_no = models.CharField(max_length=20)
    event = models.CharField(max_length=100)
    date1 = models.DateField(null=True, blank=True)
    hours1 = models.PositiveIntegerField(default=0)
    date2 = models.DateField(null=True, blank=True)
    hours2 = models.PositiveIntegerField(default=0)
    date3 = models.DateField(null=True, blank=True)
    hours3 = models.PositiveIntegerField(default=0)
    date4 = models.DateField(null=True, blank=True)
    hours4 = models.PositiveIntegerField(default=0)
    date5 = models.DateField(null=True, blank=True)
    hours5 = models.PositiveIntegerField(default=0)
    date6 = models.DateField(null=True, blank=True)
    hours6 = models.PositiveIntegerField(default=0)
    date7 = models.DateField(null=True, blank=True)
    hours7 = models.PositiveIntegerField(default=0)
    date8 = models.DateField(null=True, blank=True)
    hours8 = models.PositiveIntegerField(default=0)
    date9 = models.DateField(null=True, blank=True)
    hours9 = models.PositiveIntegerField(default=0)
    date10 = models.DateField(null=True, blank=True)
    hours10 = models.PositiveIntegerField(default=0)
    student_signature = models.CharField(max_length=100)
    teacher_signature = models.CharField(max_length=100)
    tutor_recommendation = models.CharField(max_length=100, null=True, blank=True)
    hod_remarks = models.CharField(max_length=100, null=True, blank=True)
    principal_order = models.CharField(max_length=100, null=True, blank=True)

    def total_hours(self):
        return sum([
            self.hours1, self.hours2, self.hours3, self.hours4, self.hours5,
            self.hours6, self.hours7, self.hours8, self.hours9, self.hours10
        ])
class addform(forms.ModelForm):
    class Meta:
        model = addattendance
        fields = '__all__'
