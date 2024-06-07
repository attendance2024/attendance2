from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import editattendance
from .forms import *
from student import models as studentmodel

@login_required
def teacher(request):
    return render(request, 'teacher/teacher.html')
@login_required
def home(request):
    return render(request,'teacher/teacher.html')
@login_required
def view_attendance(request):
    #event = 
    attendance_records = studentmodel.addattendance.objects.filter(request.user)
    return render(request, 'teacher/view_attendance.html', {'attendance_records': attendance_records})

@login_required
def edit_attendance(request):
    if request.method == 'POST':
        form = editattendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.student = request.user
            attendance.save()
            return redirect('view_attendance')
    else:
        form = editattendanceForm()
    return render(request, 'teacher/edit_attendance.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
