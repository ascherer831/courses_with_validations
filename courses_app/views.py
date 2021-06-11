from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
    context = {'all_courses': Course.objects.all()}

    return render(request,'index.html', context)

def courses(request):
    errors = Course.objects.new_course_validator(request.POST)
    if request.method == 'POST':
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            this_course = Course.objects.create(
                course_name = request.POST['course_name'],
                desc = request.POST['desc']
            )
            return redirect('/')
    else:
        return redirect('/')

def confirm(request,course_id):
    context ={'this_course':Course.objects.get(id=course_id)} 
    return render(request, 'confirm.html', context)

def destroy(request,course_id):
    this_course = Course.objects.get(id=course_id) 
    this_course.delete()

    return redirect('/')