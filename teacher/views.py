from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import editattendance
from .forms import *
from student import models as studentmodel
from django.contrib.auth.models import Group
# from student.models import teacher, charge 

# @login_required
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)
            
#             if user.is_principal:
#                 return redirect('principal_dashboard')
#             elif user.is_hod:
#                 return redirect('hod_dashboard')
#             elif user.is_teacher:
#                 return redirect('teacher_dashboard')
#             elif user.is_tutor:
#                 return redirect('tutor_dashboard')    
#             else:
#                 return redirect('student_dashboard')
#         else:
#             return render(request, 'login.html', {'error': 'Invalid username or password'})
    
#     return render(request, 'login.html')

# def principal_dashboard(request):
#     return HttpResponse("Principal Dashboard")

# def hod_dashboard(request):
#     return HttpResponse("HOD Dashboard")

# def teacher_dashboard(request):
#     teacher = Teacher.objects.get(user=request.user)
#     charges = Charge.objects.filter(teacher=teacher)
#     context = {'charges': charges}
#     return render(request, 'teacher_dashboard.html', context)

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
        
#         if user is not None:
#             login(request, user)
            
#             if user.is_principal:
#                 return redirect('principal_dashboard')
#             elif user.is_hod:
#                 return redirect('hod_dashboard')
#             elif user.is_teacher:
#                 return redirect('teacher_dashboard')
#             else:
#                 return redirect('student_dashboard')
#         else:
#             return render(request, 'login.html', {'error': 'Invalid username or password'})
    
#     return render(request, 'login.html')

# def principal_dashboard(request):
#     return HttpResponse("Principal Dashboard")

# def hod_dashboard(request):
#     return HttpResponse("HOD Dashboard")

# def teacher_dashboard(request):
#     teacher = teacher.objects.get(user=request.user)
#     charges = charge.objects.filter(teacher=teacher)
#     context = {'charges': charges}
#     return render(request, 'teacher_dashboard.html', context)

# def student_dashboard(request):
#     return HttpResponse("Student Dashboard")

@login_required
def teacher(request):
    context = {}
    teacher = studentmodel.teacher.objects.get(user=request.user)
    print(teacher)
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
