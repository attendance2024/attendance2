from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from weasyprint import HTML, CSS
from datetime import datetime
from .forms import *
from django.contrib.auth.models import Group
from student import models as studentmodel
from student.models import *
from django.contrib.auth.forms import UserCreationForm
from django.template.loader import render_to_string
from functools import wraps


def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_superuser:
            return render(request, 'teacher/error.html', {'message': 'You do not have permission to access this page.'})
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def group_required(group_name):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return render(request, 'teacher/error.html', {'message': 'You need to be logged in to access this page.'})
            
            if not request.user.groups.filter(name=group_name).exists():
                return render(request, 'teacher/error.html', {'message': 'You do not have permission to access this page.'})
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

@group_required('teacher')   
@login_required
def teacher_login(request):
    context = {}
    try:
        
        if request.user.is_superuser:
            context.update({'admin': True})
        else:
            context.update({'teacher': True})
        
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

@group_required('teacher')
@login_required
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

@group_required('teacher')
@login_required
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

@group_required('teacher')
@login_required
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

@group_required('teacher')
@login_required
def get_dept(request):
    # Get the teacher instance associated with the logged-in user
    teacher_instance = request.user.teacher

    # Get the department of the teacher
    dept_id = teacher_instance.dept_id

    # Filter attendance records by the department and status 'ap_by_teacher'
    attendance_records = addattendance.objects.filter(
        student__prg_id__dept_id=dept_id,
        status_id__in=['ap_by_tutor'],
    )

    context = {
        'attendance_records': attendance_records,
    }
    return render(request, 'teacher/get_hod.html', context)

@group_required('teacher')
@login_required
def get_princi(request):
    # Get the teacher instance associated with the logged-in user
    teacher_instance = request.user.teacher

    # Get the department of the teacher
    dept_id = teacher_instance.dept_id

    # Filter attendance records by the department and status 'ap_by_teacher'
    attendance_records = addattendance.objects.filter(
        status_id__in=['ap_by_hod'],
    )

    context = {
        'attendance_records': attendance_records,
    }
    return render(request, 'teacher/get_princi.html', context)


@group_required('teacher')
@login_required
def tutor_accept(request):
    att_id = request.GET.get('att_id')
    att = get_object_or_404(addattendance, id=att_id) 
    att.status_id = 'ap_by_tutor'
    att.save()
    return redirect('get_tutors')

@group_required('teacher')
@login_required
def princi_accept(request):
    att_id = request.GET.get('att_id')
    att = get_object_or_404(addattendance, id=att_id) 
    att.status_id = 'ap_by_princi'
    att.save()
    return redirect('get_princi')
@group_required('teacher')
@login_required
def hod_accept(request):
    att_id = request.GET.get('att_id')
    att = get_object_or_404(addattendance, id=att_id) 
    att.status_id = 'ap_by_hod'
    att.save()
    return redirect('get_dept')

@group_required('teacher')
@login_required
def teacher_accept(request):
    att_id = request.GET.get('att_id')
    att = get_object_or_404(addattendance, id=att_id) 
    att.status_id = 'ap_by_teacher'
    att.save()
    return redirect('get_charge')
@group_required('teacher')
@login_required
def teacher_reject(request):
    att_id = request.GET.get('att_id')
    att = get_object_or_404(addattendance, id=att_id) 
    att.status_id = 'rejected'
    att.save()
    return redirect('get_charge')

@group_required('teacher')
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@group_required('teacher')
@login_required
def generate_report(request):
    att_id = request.GET.get('att_id')
    attendance_record = get_object_or_404(addattendance, id=att_id, status_id='ap_by_princi')
    department_name = attendance_record.student.prg_id.dept_id.dept_name

    # Render the HTML template with context
    html_string = render_to_string('teacher/report_template.html', {
        'attendance_record': attendance_record,
        'department_name': department_name,
        'current_date': datetime.now().strftime('%Y-%m-%d')
    })

    # Generate PDF
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Create HTTP response with PDF content
    response = HttpResponse(result, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="report_{attendance_record.id}.pdf"'
    return response

@group_required('teacher')
@admin_required
@login_required
def addteacher(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        teacher_form = TeacherForm(request.POST)
        if user_form.is_valid() and teacher_form.is_valid():
            user = user_form.save()
            teacher = teacher_form.save(commit=False)
            teacher.user = user
            teacher.save()
            teacher_group = Group.objects.get(name='teacher')
            user.groups.add(teacher_group)
            #return redirect('home')
        
    else:
        user_form = UserCreationForm()
        teacher_form = TeacherForm()
    
    return render(request, 'teacher/create_user.html', {
        'user_form': user_form,
        'teacher_form': teacher_form,
        'teacher': True
    })

@group_required('teacher')
@admin_required
@login_required
def addstudent(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        student_form = StudentForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            student_group = Group.objects.get(name='student')
            user.groups.add(student_group)
            #return redirect('home')
        else:
            print(user_form.errors)  # Debug statement for user form errors
            print(student_form.errors)  # Debug statement for student form errors
    user_form = UserCreationForm()
    student_form = StudentForm()
    
    return render(request, 'teacher/create_user.html', {
        'user_form': user_form,
        'student_form': student_form,
        'student': True
    })
@admin_required
@login_required
def assign_teacher_position(request):
    if request.method == 'POST':
        form = TeacherPositionForm(request.POST)
        if form.is_valid():
            teacher_obj = form.cleaned_data['teacher']
            positions = form.cleaned_data['position']
            dept_id = form.cleaned_data['dept_id']
            prg_id = form.cleaned_data['prg_id']
            sem = form.cleaned_data['sem']
            ex_id = form.cleaned_data['ex_id']

            if 'incharge' in positions and ex_id:
                charge.objects.create(teacher_id=teacher_obj, ex_id=ex_id)
            if 'hod' in positions and dept_id:
                hod.objects.create(teacher_id=teacher_obj, dept_id=dept_id)
            if 'tutor' in positions and prg_id and sem:
                tutor.objects.create(teacher_id=teacher_obj, pgm_id=prg_id, sem=sem)
            if 'principal' in positions:
                principal.objects.create(teacher_id=teacher_obj)

            #return redirect('teacher_dashboard')
        else:
            # Print form errors for debugging
            print(form.errors)
    else:
        form = TeacherPositionForm()
    return render(request, 'teacher/assign_teacher_position.html', {'form': form})
