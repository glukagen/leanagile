from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from student.models import Student
from student.views import next, prev


class StudentTest(TestCase):
    name = 'test'

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
