from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import editattendance
from .forms import *
from student import models as studentmodel
#from student.models import teacher, charge 

#

@login_required
def teacher(request):
    context = {}
    try:
        teacher = studentmodel.teacher.objects.get(user=request.user)
        if studentmodel.charge.objects.filter(teacher_id=teacher).exists():
            charge = studentmodel.charge.objects.filter(teacher_id=teacher).first()
            context.update({'charge':charge})

        if studentmodel.hod.objects.filter(teacher_id=teacher).exists():
            dept = studentmodel.hod.objects.filter(teacher_id=teacher).first()
            context.update({'hod':dept})

        if studentmodel.tutor.objects.filter(teacher_id=teacher).exists():
            tutor_class = studentmodel.tutor.objects.filter(teacher_id=teacher).first()
            context.update({'tutor':tutor_class})

        if Group.objects.get(name='principal') in request.user.groups.all():
            context.update({"principal":1})
    except:
        pass
    return render(request, 'teacher/teacher.html',context)










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
