from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os


class Student(models.Model):
    user = models.OneToOneField(User, related_name="student")
    full_name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='./',
                max_length=500, null=True, blank=True)
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

    def set_photo(self, image):
        if self.image:
            os.remove("%s/%s" % (settings.MEDIA_ROOT, self.image.name))
        self.image = image
        self.save()

    @property
    def categories(self):
        from skill.models import Category
        categories = Category.objects.all()
        for category in categories:
            category.our_tracks = []
            for track in category.tracks.all():
                category.our_tracks.append(track)
                track_index = len(category.our_tracks) - 1
                category.our_tracks[track_index].our_skills = []
                for skill in category.our_tracks[track_index].skills.all():
                    status = self.statuses.get(skill=skill)
                    skill.status = status.value
                    skill.status_id = status.id
                    category.our_tracks[track_index].our_skills.append(skill)
        return categories

    @property
    def levels(self):
        from skill.models import ProgressLevel
        levels = ProgressLevel.objects.all()
        status_is_set = False
        for level in levels:
            if status_is_set:
                level.status = 'n'
            elif level == self.progress_stasus.level:
                level.status = self.progress_stasus.value
                status_is_set = True
            else:
                level.status = 'd'
        return levels

    def save(self):
        self.full_name = "%s %s" % (self.user.last_name, self.user.first_name)
        super(Student, self).save()

    def __str__(self):
        return self.user.get_full_name()
