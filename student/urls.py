from django.urls import path
from . import views
urlpatterns = [
   
    path('studentlogin/',views.StudentLogin,name='student'),
    path('',views.home,name='home'),
    path('add_attendance/', views.add_attendance, name='add_attendance'),
    path('filter_events/', views.filter_events, name='filter_events'),
    path('viewattendance/',views.view_attendance,name='student_view_attendance'),
    path('success/',views.success,name='success'),
    path('about/',views.aboutcollege,name='aboutcollege'),
]
