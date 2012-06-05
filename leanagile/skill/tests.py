from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from student.models import Student
from skill.models import SkillStatus, Skill, Track, Category, \
    ProgressLevel, ProgressStatus


class SkillAjaxTest(TestCase):
    name = "test"

    def setUp(self):
        user = User(first_name=self.name,
            last_name=self.name, username=self.name)
        user.save()
        self.student = Student(user=user, about_me=self.name,
            specialities=self.name)
        self.student.save()

    def test_change_status(self):
        category = Category(name=self.name)
        category.save()

        track = Track(name=self.name, category=category)
        track.save()

        skill = Skill(name=self.name, track=track)
        skill.save()

        #value = 'n'
        status = SkillStatus(student=self.student, skill=skill)
        status.save()

        response = self.client.get(reverse('change-skill-status',
                    args=(status.id,)))
        # should be 'i'
        self.assertEqual(response.status_code, 200)
        self.assertEqual(SkillStatus.objects.get(id=status.id).value, 'i')

    def test_change_progress_status(self):
        level = ProgressLevel(name=self.name)
        level.save()

        response = self.client.post(reverse('change-progress-status',
                args=(self.student.progress_stasus.id,)),
                data={'value': 'i', 'level': level.id, })

        self.assertEqual(response.status_code, 200)
        updated_status = ProgressStatus.objects.get(
                        id=self.student.progress_stasus.id)

        self.assertEqual(updated_status.value, 'i')
        self.assertEqual(updated_status.level, level)
