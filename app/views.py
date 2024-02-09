from django.shortcuts import render
from app.models import *
from django.views.generic import ListView
# Create your views here.


class StudentList(ListView):
    model=School
    context_object_name='schools'
    ordering=['sname']
    #qureyset=School.objects.filter(id=1)
    #template_name='app/School_list.html'
