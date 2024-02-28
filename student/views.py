from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
# Create your views here.
def index(request):
    return HttpResponse("Hello World")

def college(request):
    return render(request,'student/index.html')  

def StudentLogin(request):
    if request.method == "POST":
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
    forms = studentform()
    return render(request,'student/student.html',{'form':forms}) 

def home(request):
    return render(request,'student/home.html')

def teacher(request):
    forms = teacherform()
    return render(request,'student/teacher.html',{'form':forms})

def tutor(request):
    forms = studentform()
    return render(request,'student/tutor.html',{'form':forms})  

def hod(request):
    forms = hodform()
    return render(request,'student/hod.html',{'form':forms})  

def contact(request):
    return render(request,'student/contact.html')    