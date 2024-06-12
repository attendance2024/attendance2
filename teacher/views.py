from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import editattendance
from .forms import *
from django.contrib.auth.models import Group
from student import models as studentmodel
from student.models import *

#

@login_required
def teacher(request):
    context = {}
    try:
        teacher = studentmodel.teacher.objects.get(user=request.user)
        
        charge = studentmodel.charge.objects.filter(teacher_id=teacher).first()
        if charge:
            context.update({'charge': charge})

        dept = studentmodel.hod.objects.filter(teacher_id=teacher).first()
        if dept:
            context.update({'hod': dept})

        tutor_class = studentmodel.tutor.objects.filter(teacher_id=teacher).first()
        if tutor_class:
            context.update({'tutor': tutor_class})

        if request.user.groups.filter(name='principal').exists():
            context.update({"principal": 1})

    except studentmodel.teacher.DoesNotExist:
        pass

    return render(request, 'teacher/teacher.html', context)


def get_charge(request):
    # Assuming the logged-in teacher is in charge of an event
    teacher = request.user.teacher
    charge_obj = charge.objects.get(teacher_id=teacher)
    ex_id = charge_obj.ex_id

    # Fetch students' attendance related to the event
    attendance_records = addattendance.objects.filter(event__ex_id=ex_id)

    context = {
        'attendance_records': attendance_records,
    }
    return render(request, 'teacher/get_charge.html', context)

def add_event(request):
    try:
        teacher_instance = get_object_or_404(teacher, user=request.user)
        charge_instance = get_object_or_404(charge, teacher_id=teacher_instance)
        initial_data = {'ex_id': charge_instance.ex_id}
    except charge.DoesNotExist:
        initial_data = {}
        
    if request.method == 'POST':
        form = EventForm(request.POST, initial=initial_data)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to the event list page after adding the event
    else:
        form = EventForm(initial=initial_data)
    return render(request, 'add_event.html', {'form': form})

def get_dept(request):
    # Get the teacher instance associated with the logged-in user
    teacher_instance = request.user.teacher

    # Get the department of the teacher
    dept_id = teacher_instance.dept_id

    # Filter attendance records by the department and status 'ap_by_teacher'
    attendance_records = addattendance.objects.filter(
        student__prg_id__dept_id=dept_id,
        status_id__in=['ap_by_hod', 'ap_by_tutor'],
    )

    context = {
        'attendance_records': attendance_records,
    }
    return render(request, 'teacher/get_hod.html', context)


def get_tutors(request):
    # Get the teacher instance associated with the logged-in user
    teacher_instance = request.user.teacher

    # Get the department of the teacher
    dept_id = teacher_instance.dept_id

    # Get the tutor instance associated with the teacher
    tutor_instance = tutor.objects.filter(teacher_id=teacher_instance).first()  # Get the first tutor instance

    if tutor_instance:
        tutor_sem = tutor_instance.sem

        # Filter attendance records by department, status 'ap_by_teacher', and matching semester
        attendance_records = addattendance.objects.filter(
            student__prg_id__dept_id=dept_id,
            status_id__in=['ap_by_teacher', 'ap_by_tutor'],
            student__current_sem=tutor_sem
        )
    else:
        attendance_records = []

    context = {
        'attendance_records': attendance_records,
    }
    return render(request, 'teacher/get_dept.html', context)

def tutor_accept(request):
    att_id = request.GET.get('att_id')
    att = get_object_or_404(addattendance, id=att_id) 
    att.status_id = 'ap_by_tutor'
    att.save()
    return redirect('get_tutors')

def hod_accept(request):
    att_id = request.GET.get('att_id')
    att = get_object_or_404(addattendance, id=att_id) 
    att.status_id = 'ap_by_hod'
    att.save()
    return redirect('get_dept')



def teacher_accept(request):
    att_id = request.GET.get('att_id')
    att = get_object_or_404(addattendance, id=att_id) 
    att.status_id = 'ap_by_teacher'
    att.save()
    return redirect('get_charge')


def teacher_reject(request):
    att_id = request.GET.get('att_id')
    att = get_object_or_404(addattendance, id=att_id) 
    att.status_id = 'rejected'
    att.save()
    return redirect('get_charge')


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
