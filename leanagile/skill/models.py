from django.db import models
from student.models import Student


class Category(models.Model):
    name = models.CharField(max_length=32)


class Track(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255, blank=True, null=True)

        
class Skill(models.Model):
    track = models.ForeignKey(Track)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255, blank=True, null=True)


class SkillStatus(models.Model):
    skill = model.ForeignKey(Skill)
    student = models.ForeignKey(Student)
    STATUS_CHOICES = (
        ('n', u'Not started'),
        ('i', u'In progress'),
        ('d', u'Done'),
    )
    value = models.CharField(max_length=1, choices=STATUS_CHOICES, default='n')