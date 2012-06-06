from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from leanagile.decorators import render_to
from student.forms import StudentForm
from student.models import Student
from skill.models import Category, ProgressLevel
import uuid


@render_to('student/add.html')
def add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
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
                specialities=request.POST['specialities'],
                about_me=request.POST['about_me']
            )
            if request.FILES.get('photo'):
                student.image = request.FILES['photo']
            student.save()
            return redirect(reverse('student-profile', args=(student.id,)))
    else:
        form = StudentForm()
    return locals()


def upload_photo(request, id):
    if not request.FILES.get('photo'):
        raise Http404

    student = get_object_or_404(Student, pk=id)
    student.set_photo(request.FILES['photo'])
    return HttpResponse(student.avatar)


def edit(request, id):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = get_object_or_404(Student, pk=id)
            student.user.first_name = request.POST['first_name']
            student.user.last_name = request.POST['last_name']
            student.user.save()
            student.about_me = request.POST['about_me']
            student.specialities = request.POST['specialities']
            student.save()
            return HttpResponse('1')
    return HttpResponse('0')


def next(student):
    try:
        next_student = Student.objects.filter(
                    full_name__gt=student.full_name)[0]
    except:
        return None
    return next_student.id


def prev(student):
    try:
        prev_student = Student.objects.filter(
                    full_name__lt=student.full_name)[0]
    except:
        return None
    return prev_student.id


@render_to('student/profile.html')
def profile(request, id):
    student = get_object_or_404(Student, pk=id)
    next_student = next(student)
    prev_student = prev(student)
    return locals()


def delete(request, id):
    try:
        student = Student.objects.get(pk=id)
        id = prev(student)
        student.delete()
        return HttpResponse(id if id else '-1')
    except:
        return HttpResponse('0')


def first(request):
    try:
        student = Student.objects.all()[:1][0]
    except:
        raise Http404
    return redirect(reverse('student-profile', args=(student.id,)))


def last(request):
    try:
        student = Student.objects.all().reverse()[:1][0]
    except:
        raise Http404
    return redirect(reverse('student-profile', args=(student.id,)))
