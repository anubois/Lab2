from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm



def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = StudentForm()

    return render(request, 'form.html', {'form': form})



def show_student(request):
    data = Student.objects.all()
    return render(request, 'show.html', {'data': data})



def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('show')
    else:
        form = StudentForm(instance=student)

    return render(request, 'form.html', {'form': form})



def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('show')