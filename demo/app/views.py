from django.shortcuts import render
from .models import Student

# Create your views here.

def home(request):
    context = {'title':'Homepage','intro':'Student Information'}
    return render(request,'home.html',context)

def about(request):
    students = Student.objects.all()
    return render(request, 'about.html', {'students': students})

from django.shortcuts import render, redirect
from .forms import StudentForm

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about')  # Replace with your success URL
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

