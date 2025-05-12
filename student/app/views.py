from django.shortcuts import render
from .models import Student
from django.http import HttpResponse

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

def delete_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        
        # Validate if the student exists
        try:
            student = Student.objects.get(name=name, phno=phone_number)
            student.delete()
            return redirect('home')
        except Student.DoesNotExist:
            return redirect('home')    
    return render(request, 'delete_student.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def delete_student_directly(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':  # Confirm deletion
        student.delete()
        return redirect('about')  # Redirect to the page showing the list of students
    return render(request, 'about.html', {'student': student})