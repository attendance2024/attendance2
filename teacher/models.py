from django.db import models
from django.contrib.auth.models import User

class editattendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')],null=True)
    hours = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f"{self.student.username} - {self.date} - {self.status} - {self.hours} hours"
