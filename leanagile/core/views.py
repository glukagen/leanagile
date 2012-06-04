from django.shortcuts import redirect
from annoying.decorators import render_to
from django.db.models import Q

from student.models import Student


def index(request):
    return redirect('student-first' if Student.objects.count()  else 'student-add')


@render_to('search.html')
def search(request):
    s = request.GET.get('s')
    if not s:
        return redirect('index')
    
    students = Student.objects.filter(
        Q(user__first_name__icontains=s) | 
        Q(user__last_name__icontains=s) | 
        Q(about_me__icontains=s) |
        Q(specialities__icontains=s) 
    )
    
    return locals()

