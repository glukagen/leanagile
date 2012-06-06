from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from student.models import Student


class CoreTest(TestCase):
    name = "core_test"

    def test_index(self):
        def do_request(redirect):
            response = self.client.get(reverse('index'))
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response,
                    'http://testserver%s' % reverse(redirect))

        do_request('student-add')
        user = User(username=self.name)
        user.save()

        student = Student(user=user, specialities=self.name)
        student.save()

        #do_request('student-first')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 302)

    def test_search(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('search'), data={'s': 'a'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
