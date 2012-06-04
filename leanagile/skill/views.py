from django.http import HttpResponse
from skill.models import SkillStatus, ProgressLevelStatus


def change_status(request, status_id):
    try:
        SkillStatus.objects.get(id=status_id).change()
        return HttpResponse('1')
    except:
        return Httpresponse('0')
    

def change_progress_status(request, status_id):
    try:
        ProgressLevelStatus.objects.get(id=status_id).change()
        return HttpResponse('1')
    except:
        return Httpresponse('0')
