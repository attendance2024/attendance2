from django.db import models
from django.conf import settings
from django import forms
# Create your models here.
class department(models.Model):
    dept_name = models.CharField(max_length=120)
    
    
    def __str__(self):
        return self.dept_name

class programme(models.Model):
    pgm_name = models.CharField(max_length=120)
    dept_id = models.ForeignKey(department,on_delete=models.CASCADE)
    grad_level = models.CharField(max_length=120)
    def __str__(self):
        return self.pgm_name
  
class student(models.Model):
    reg_no = models.CharField(max_length=10)
    student_name = models.CharField(max_length=120)
    adm_no = models.IntegerField()
    email = models.EmailField()
    year_of_adm = models.IntegerField()
    current_sem = models.IntegerField()
    contact_number = models.CharField(max_length=10)
    prg_id = models.ForeignKey(programme,on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.student_name
class extra_curricular_activities(models.Model):
    ex_name = models.CharField(max_length=120)
    def __str__(self):
        return self.ex_name
class event(models.Model):
    ex_id = models.ForeignKey(extra_curricular_activities,on_delete=models.CASCADE)
    event_description = models.CharField(max_length=120)
class teacher(models.Model):
    teacher_name = models.CharField(max_length=120)
    dept_id = models.ForeignKey(department,on_delete=models.CASCADE)
    def __str__(self):
        return self.teacher_name
class charge(models.Model):
    teacher_id = models.ForeignKey(teacher,on_delete=models.CASCADE)   
    ex_id = models.ForeignKey(extra_curricular_activities,on_delete=models.CASCADE)

class status(models.Model):
    status_descr = models.CharField(max_length=120)
class addattendance(models.Model):
    event = models.ForeignKey(event,on_delete=models.CASCADE)
    student = models.ForeignKey(student,on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.SmallIntegerField(null=True)
    status_id = models.ForeignKey(status,on_delete=models.CASCADE)


class tutor(models.Model):
    pgm_id = models.ForeignKey(programme,on_delete=models.CASCADE)
    sem = models.IntegerField()
    teacher_id = models.ForeignKey(teacher,on_delete=models.CASCADE)
class hod(models.Model):
    teacher_id = models.ForeignKey(teacher,on_delete=models.CASCADE)
    dept_id = models.ForeignKey(department,on_delete=models.CASCADE)
     
class addform(forms.ModelForm):
    class Meta:
        model = addattendance
        fields = '__all__'
