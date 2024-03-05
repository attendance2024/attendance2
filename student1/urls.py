from django.urls import path
from . import views
urlpatterns = [
    path('studentlogin/',views.studentlogin,name='student1')
]
