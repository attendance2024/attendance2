from django.shortcuts import render,redirect
from .models import addattendance
from django.http import HttpResponse
from .forms import *
# Create your views here.


def college(request):
    return render(request,'student/index.html')  

def StudentLogin(request):
    if request.method == "POST":
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
    forms = studentform()
    return render(request,'student/student.html',{'form':forms}) 

def home(request):
    return render(request,'student/home.html')

def add_attendance(request):
    if request.method == 'POST':
        form = addform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success') 
    else:
        form = addform()
    return render(request, 'student/add_attendance.html', {'form': form})
def view_attendance(request):
    attendance_records = addattendance.objects.all()
    return render(request, 'student/view_attendance.html', {'attendance_records': attendance_records})
def success(request):
    return render(request,'student/success.html') 