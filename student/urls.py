from django.urls import path
from . import views
urlpatterns = [
   
    path('studentlogin/',views.StudentLogin,name='student'),
    path('',views.home,name='home'),
    path('addattendance/',views.add_attendance,name='add_attendance'),
    path('viewattendance/',views.view_attendance,name='student_view_attendance'),
    path('success/',views.success,name='success'),
]
