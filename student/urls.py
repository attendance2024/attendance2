from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('college/',views.college,name='college'),
    path('studentlogin/',views.StudentLogin,name='student'),
    path('home/',views.home,name='home'),
    path('teacher/',views.teacher,name='teacher'),
    path('tutor/',views.tutor,name='tutor'),
    path('hod/',views.hod,name='hod'),
    path('principal/',views.principal,name='principal'),
    path('contact/',views.contact,name='contact'),
]
