from django.http import HttpResponse
from skill.models import SkillStatus

def change_status(request, status_id):
    try:
        SkillStatus.objects.get(id=status_id).change()
        return HttpResponse('1')
    except:
        return Httpresponse('0')
