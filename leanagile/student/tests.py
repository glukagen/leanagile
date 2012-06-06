from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from student.models import Student
from student.views import next, prev
from student.forms import StudentForm


class StudentTest(TestCase):
    name = 'test'
    data = {
        'first_name': "a",
        'last_name': "b",
        'about_me': "c",
        'specialities': "d",
    }

    def _create_student(self, prefix=''):
        name = "%s_%s" % (self.name, prefix)
        user = User(first_name=name, last_name=name, username=name)
        user.save()
        student = Student(user=user, about_me=name, specialities=name)
        student.save()
        return student

    def setUp(self):
        self.first_student = self._create_student('_a')
        self.student = self._create_student('_b')
        self.last_student = self._create_student('_c')

    def test_last(self):
        response = self.client.get(reverse('student-last'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, 'http://testserver%s' % reverse(
                    'student-profile', args=(str(self.last_student.id),)))

    def test_first(self):
        response = self.client.get(reverse('student-first'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, 'http://testserver%s' % reverse(
                    'student-profile', args=(str(self.first_student.id),)))

    def test_delete(self):
        student = self._create_student()
        response = self.client.get(reverse('student-delete',
                                           args=(str(student.id),)))
        self.assertEqual(Student.objects.filter(id=student.id).count(), 0)

    def test_profile(self):
        response = self.client.get(reverse('student-profile',
                                args=(str(self.student.id),)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/profile.html')

        response = self.client.get(reverse('student-profile',
                                args=('0'),))
        self.assertEqual(response.status_code, 404)

    def test_next(self):
        self.assertEqual(next(self.student), self.last_student.id)
        self.assertEqual(next(self.last_student), None)

    def test_prev(self):
        self.assertEqual(prev(self.student), self.first_student.id)
        self.assertEqual(prev(self.first_student), None)

    def test_edit(self):
        url = reverse('student-edit', args=(str(self.student.id)))
        response = self.client.post(url, data=self.data)
        self.assertEqual(response.status_code, 200)
        student = Student.objects.get(pk=self.student.id)
        self.assertEqual(student.about_me, self.data['about_me'])
        self.assertEqual(student.specialities, self.data['specialities'])
        self.assertEqual(student.user.first_name, self.data['first_name'])
        self.assertEqual(student.user.last_name, self.data['last_name'])

    def test_add(self):
        response = self.client.get(reverse('student-add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student/add.html')
        self.failUnless(isinstance(response.context['form'], StudentForm))

        count = Student.objects.count()
        response = self.client.post(reverse('student-add'), data=self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Student.objects.count(), count + 1)

        student = Student.objects.order_by('-id')[:1][0]
        self.assertEqual(student.about_me, self.data['about_me'])
        self.assertEqual(student.specialities, self.data['specialities'])
        self.assertEqual(student.user.first_name, self.data['first_name'])
        self.assertEqual(student.user.last_name, self.data['last_name'])
        self.assertRedirects(response, 'http://testserver%s' % reverse(
                    'student-profile', args=(str(student.id),)))
