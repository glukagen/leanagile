from django.db import models
from django.db.models.signals import post_save
from student.models import Student


class AbstractCategory(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class AbstractSkill(AbstractCategory):
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        abstract = True


class Category(AbstractCategory):
    pass


class Track(AbstractSkill):
    category = models.ForeignKey(Category, related_name='tracks')


class Skill(AbstractSkill):
    track = models.ForeignKey(Track, related_name='skills')


class AbstractStatus(models.Model):
    STATUS_CHOICES = (
        ('n', u'Not started'),
        ('i', u'In progress'),
        ('d', u'Done'),
    )
    value = models.CharField(max_length=1, choices=STATUS_CHOICES, default='n')

    class Meta:
        abstract = True

    def change(self):
        self.value = 'i' if self.value == 'n' else 'd' \
            if self.value == 'i' else 'n'
        self.save()


class ProgressLevel(AbstractCategory):
    pass


class ProgressStatus(AbstractStatus):
    student = models.OneToOneField(Student, related_name='progress_stasus')
    level = models.ForeignKey(ProgressLevel)


class SkillStatus(AbstractStatus):
    skill = models.ForeignKey(Skill)
    student = models.ForeignKey(Student, related_name='statuses')


def create_student(sender, instance, created, **kwargs):
    if created:
        for skill in Skill.objects.all():
            SkillStatus(student=instance, skill=skill).save()
        ProgressStatus(student=instance,
            level=ProgressLevel.objects.all()[:1][0]).save()


models.signals.post_save.connect(create_student, sender=Student)
