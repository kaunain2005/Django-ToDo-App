from django.shortcuts import render, redirect

from .forms import StudentAdmissionForm
from .models import Student


def home(request):
    return render(request, "core/home.html")


def students(request):
    students = Student.objects.all()
    return render(request, "core/students.html", {"students": students})


def admit_student(request):
    if request.method == 'POST':
        form = StudentAdmissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:students')
    else:
        form = StudentAdmissionForm()

    return render(request, 'core/admit_student.html', {'form': form})
