from django.urls import path
from . import views
urlpatterns = [
    path('', views.teacher, name='teacher'),
    path('viewattendance/', views.view_attendance, name='view_attendance'),
    path('editattendance/', views.edit_attendance, name='edit_attendance'),
]
