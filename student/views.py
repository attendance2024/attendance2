from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def college(request):
    forms = studentform()
    return render(request,'student/index.html',{'form':forms})  

def StudentLogin(request):
    return render(request,'student/student.html') 

def home(request):
    return render(request,'student/home.html')

def teacher(request):
    return render(request,'student/teacher.html')

def tutor(request):
    return render(request,'student/tutor.html')  

def hod(request):
    return render(request,'student/hod.html')  

def principal(request):
    return render(request,'student/principle.html')

def contact(request):
    return render(request,'student/contact.html')    