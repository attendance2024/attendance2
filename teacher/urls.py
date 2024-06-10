from django.urls import path
from . import views
urlpatterns = [
    path('', views.teacher, name='teacher'),
    path('viewattendance/', views.view_attendance, name='view_attendance'),
    path('editattendance/', views.edit_attendance, name='edit_attendance'),
    path('login/', views.login_view, name='login'),
    path('principal_dashboard/', views.principal_dashboard, name='principal_dashboard'),
    path('hod_dashboard/', views.hod_dashboard, name='hod_dashboard'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
]
