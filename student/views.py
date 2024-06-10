from django.shortcuts import render,redirect
from .models import addattendance
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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

def success_view(request):
    return render(request, 'student/success.html')


def home(request):
    return render(request,'student/home.html')

@login_required()
def add_attendance(request):
    context = {
        'eve': event.objects.all()
    }
    if request.method == 'POST':
        evet_description = request.POST.get('event')
        event_instance = event.objects.get(event_description=evet_description)
        student_instance = student.objects.get(user=request.user)
        date = request.POST.get('date')
        hours = request.POST.getlist('hour')
        totalhour = request.POST.get('totalhours')
        
        for hour in hours:
            attendance = addattendance(
                event=event_instance,
                student=student_instance,
                date=date,
                hour=hour,
                totalhour=totalhour
            )
            attendance.save()
        return redirect('success')
    
    return render(request, 'student/add_attendance.html', context)

@login_required()    
def view_attendance(request):
    attendance_records = addattendance.objects.all()
    print(attendance_records)
    return render(request, 'student/view_attendance.html', {'attendance_records': attendance_records})
@login_required()    
def success(request):
    return render(request,'student/success.html') 