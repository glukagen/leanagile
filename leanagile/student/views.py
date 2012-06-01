from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from annoying.decorators import render_to
from student.forms import StudentForm
from student.models import Student
import uuid


@render_to('student/add.html')
def add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        print form.is_valid()        
        if form.is_valid():
            
            user = User(
                 first_name=request.POST['first_name'],
                 last_name=request.POST['last_name']
            )
            user.username = "%s_%s_%s" % (user.first_name,
                user.last_name, str(uuid.uuid4()).replace('-', '')[:8])
            user.save()
            
            student = Student(
                user=user,
                image=request.FILES['photo'],
                specialities=request.POST['specialities'],
                about_me=request.POST['about_me']
            )
            student.save()
            return redirect(reverse('student-profile', args=(student.id,)))
    else:
        form = StudentForm()    
    return locals()


@render_to('student/profile.html')
def profile(request, id):
    student = get_object_or_404(Student, pk=id)
    return locals()

