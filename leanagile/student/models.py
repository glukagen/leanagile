from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 


class Student(models.Model):
    user = models.OneToOneField(User, related_name="student")
    full_name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='./', max_length=500, null=True, blank=True)
    specialities = models.CharField(max_length=255, null=True, blank=True)
    about_me = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        ordering = ['full_name', ]
        
    @property
    def avatar(self):
        if self.image:
            return "%s%s" % (settings.MEDIA_URL, self.image.name)
        else:
            return '%sassets/img/user-avatar.jpg' % settings.STATIC_URL
        
    
    def save(self):
        self.full_name = "%s %s" % (self.user.last_name, self.user.first_name)
        super(Student, self).save()
    
    def __str__(self):
        return self.user.get_full_name()