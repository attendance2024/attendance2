from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def teacherlogin(request):
    return render(request,'teacher1/index2.html') 

