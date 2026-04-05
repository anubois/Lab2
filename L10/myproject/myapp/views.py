from django.shortcuts import render
from .models import Student

def show_student(request):
    data = Student.objects.all()
    return render(request, 'index.html', {'data': data})