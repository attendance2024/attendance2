from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher, name='teacher'),
    path('viewattendance/', views.view_attendance, name='view_attendance'),
    path('editattendance/', views.edit_attendance, name='edit_attendance'),
    path('get_charge/', views.get_charge, name='get_charge'),
    path('get_dept/', views.get_dept, name='get_dept'),
    path('get_tutor/', views.get_tutors, name='get_tutors'),
    path('teacher_accept/',views.teacher_accept, name='teacher_accept'),
    path('teacher_reject/',views.teacher_reject, name='teacher_reject'),
    path('tutor_accept/',views.tutor_accept, name='tutor_accept'),
    path('hod_accept/',views.hod_accept, name='hod_accept'),
    path('add_event/',views.add_event, name='add_event'),
   # path('login/', views.login_view, name='login'),
    #path('principal_dashboard/', views.principal_dashboard, name='principal_dashboard'),
    #path('hod_dashboard/', views.hod_dashboard, name='hod_dashboard'),
    #path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
]
