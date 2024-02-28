from django.urls import path
from . import views
urlpatterns = [
    path('principallogin/',views.principallogin,name='principal'),
    
]
