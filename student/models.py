from django.db import models
from django.conf import settings
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