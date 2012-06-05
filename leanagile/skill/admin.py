from django.contrib import admin
from skill.models import Skill, Track, Category, ProgressLevel


class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'track', )


admin.site.register(Skill, SkillAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Category)
admin.site.register(ProgressLevel)
