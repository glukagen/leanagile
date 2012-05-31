from annoying.decorators import render_to
from student.forms import StudentForm

@render_to('student/student-add.html')
def add(request):
    form = StudentForm()
    return locals()
