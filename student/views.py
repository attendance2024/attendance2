from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.



@login_required()
def StudentLogin(request):
    if request.method == "POST":    
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
    forms = studentform()
    return render(request,'student/student.html',{'form':forms}) 

@login_required()
def success_view(request):
    return render(request, 'student/success.html')


def home(request):
    return render(request,'student/base.html')

@login_required()
def add_attendance(request):
    context = {
        'activities': extra_curricular_activities.objects.all()
    }
    if request.method == 'POST':
        event_description = request.POST.get('event')
        event_instance = event.objects.get(event_description=event_description)
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
def filter_events(request):
    extracurricular_id = request.GET.get('extracurricular_id')
    events = event.objects.filter(ex_id=extracurricular_id).values('event_description')
    return JsonResponse({'events': list(events)})


@login_required()    
def view_attendance(request):
    stud = student.objects.filter(user=request.user).first()
    attendance_records = addattendance.objects.filter(student=stud)
    return render(request, 'student/view_attendance.html', {'attendance_records': attendance_records})
@login_required()    
def success(request):
    return render(request,'student/success.html') 
  
def aboutcollege(request):
    return render(request, 'student/about.html')
