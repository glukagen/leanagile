from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, related_name="student")
    image = models.ImageField(upload_to='./media/', max_length=500, null=True, blank=True)
    specialities = models.CharField(max_length=255, null=True, blank=True)
    about_me = models.CharField(max_length=255, null=True, blank=True)
