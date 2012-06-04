from student.models import Student
from django.shortcuts import redirect


def index(request):
    return redirect('student-first' if Student.objects.count()  else 'student-add')

