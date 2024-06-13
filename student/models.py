#student/models.py


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
    event_description = models.CharField(max_length=120, unique=True)
    def __str__(self):
        return self.event_description

    def save(self, *args, **kwargs):
        # Convert email to lowercase before saving
        self.event_description = self.event_description.lower()
        super(event, self).save(*args, **kwargs)

    
class teacher(models.Model):
    teacher_name = models.CharField(max_length=120)
    dept_id = models.ForeignKey(department,on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.teacher_name
class charge(models.Model):
    teacher_id = models.ForeignKey(teacher,on_delete=models.CASCADE)   
    ex_id = models.ForeignKey(extra_curricular_activities,on_delete=models.CASCADE)

class status(models.Model):
    status_descr = models.CharField(max_length=120)
    def __str__(self):
        return self.status_descr
class addattendance(models.Model):
    Status = [
        ('pending','pending'),
        ('rejected','rejected'),
        ('ap_by_teacher','ap_by_teacher'),
        ('ap_by_tutor','ap_by_tutor'),
        ('ap_by_hod','ap_by_hod'),
        ('ap_by_princi','ap_by_princi'),
        ('ap_by_tutor_2','ap_by_tutor_2')
        
    ]
    event = models.ForeignKey(event,on_delete=models.CASCADE)
    student = models.ForeignKey(student,on_delete=models.CASCADE)
    date = models.DateField()
    hour = models.SmallIntegerField(null=True)
    totalhour = models.IntegerField(default=1)
    status_id = models.CharField(max_length=15, choices=Status, default='pending')


    def __str__(self):
        return f"Attendence - {self.student.student_name} - {self.event.ex_id} - {self.event.event_description} - {self.status_id}"



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


class principal(models.Model):
    teacher_id = models.ForeignKey(teacher, on_delete=models.CASCADE)