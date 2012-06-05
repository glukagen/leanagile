from django.http import HttpResponse
from skill.models import SkillStatus, ProgressStatus, ProgressLevel
from django.shortcuts import get_object_or_404


def change_status(request, status_id):
    try:
        SkillStatus.objects.get(id=status_id).change()
        return HttpResponse('1')
    except:
        return Httpresponse('0')


def change_progress_status(request, status_id):
    try:
        status = ProgressStatus.objects.get(id=status_id)
        status.level = get_object_or_404(
                ProgressLevel, pk=request.POST.get('level'))
        status.value = request.POST.get('value')
        status.save()
        return HttpResponse('1')
    except:
        return Httpresponse('0')
