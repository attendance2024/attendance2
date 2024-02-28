from django.urls import path
from . import views
urlpatterns = [
    path('teacherlogin/',views.teacherlogin,name='teacher'),
    
]
