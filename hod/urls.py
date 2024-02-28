from django.urls import path
from . import views
urlpatterns = [
    path('hodlogin/',views.hodlogin,name='hod'),
    
]
