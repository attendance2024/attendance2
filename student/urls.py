from django.urls import path
from . import views
urlpatterns = [
    path('college/',views.college,name='college'),
    path('studentlogin/',views.StudentLogin,name='student'),
    path('',views.home,name='home'),
    path('teacher/',views.teacher,name='teacher'),
    path('tutor/',views.tutor,name='tutor'),
    path('hod/',views.hod,name='hod'),
    
    path('contact/',views.contact,name='contact'),
]
