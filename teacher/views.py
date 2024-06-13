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
def teacher_login(request):
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

        if studentmodel.principal.objects.filter(teacher_id=teacher).exists():
            context.update({"principal": 1})

    except studentmodel.teacher.DoesNotExist:
        pass

    return render(request, 'teacher/teacher.html', context)

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
            status_id__in=['ap_by_teacher', 'ap_by_tutor', 'ap_by_princi'],
            student__current_sem=tutor_sem
        )
    else:
        attendance_records = []

    context = {
        'attendance_records': attendance_records,
    }
    return render(request, 'teacher/get_dept.html', context)

def add_event(request):
    teacher_instance = teacher.objects.filter(user=request.user).first()
    charge_instance = charge.objects.filter(teacher_id=teacher_instance).first() if teacher_instance else None
    initial_data = {'ex_id': charge_instance.ex_id} if charge_instance else {}

    if request.method == 'POST':
        form = EventForm(request.POST, initial=initial_data)
        if form.is_valid():
            form.save()
            return redirect('get_charge')
    else:
        form = EventForm(initial=initial_data)

    return render(request, 'teacher/add_event.html', {'form': form})

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


def get_princi(request):
    # Get the teacher instance associated with the logged-in user
    teacher_instance = request.user.teacher

    # Get the department of the teacher
    dept_id = teacher_instance.dept_id

    # Filter attendance records by the department and status 'ap_by_teacher'
    attendance_records = addattendance.objects.filter(
        status_id__in=['ap_by_hod', 'ap_by_princi'],
    )

    context = {
        'attendance_records': attendance_records,
    }
    return render(request, 'teacher/get_princi.html', context)




def tutor_accept(request):
    att_id = request.GET.get('att_id')
    att = get_object_or_404(addattendance, id=att_id) 
    att.status_id = 'ap_by_tutor'
    att.save()
    return redirect('get_tutors')

def princi_accept(request):
    att_id = request.GET.get('att_id')
    att = get_object_or_404(addattendance, id=att_id) 
    att.status_id = 'ap_by_princi'
    att.save()
    return redirect('get_princi')

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


def generate_report(request):
    att_id = request.GET.get('att_id')
    attendance_record = get_object_or_404(addattendance, id=att_id, status_id='ap_by_princi')

    # Create a report (for simplicity, we'll just create a text report)
    report_content = f"""
    Attendance Report
    -----------------
    Student Name: {attendance_record.student.student_name}
    Registration Number: {attendance_record.student.reg_no}
    Event: {attendance_record.event.event_description}
    Date: {attendance_record.date}
    Hour: {attendance_record.hour}
    Status: Approved By Pricipal 
    """

    # Create an HTTP response with the report content
    response = HttpResponse(report_content, content_type='text/plain')
    response['Content-Disposition'] = f'attachment; filename="report_{attendance_record.id}.txt"'

    return response