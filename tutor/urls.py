from django.urls import path
from . import views
urlpatterns = [
    path('tutorlogin/',views.tutorlogin,name='tutor'),
    
]
