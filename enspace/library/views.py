import datetime
from django.utils import timezone
from django.http import Http404
from django.shortcuts import render
from . import models
# Create your views here.
def library_home_view(request):
    rlo = models.LearningObject.objects.filter(
        timestamp__gte=timezone.now() - datetime.timedelta(days=7))
    context = {
        'recent_learning_objects': rlo,
    }
    return render(request, 'library/main.html', context)

def library_item(request, item_id):
    try:
        item = models.LearningObject.objects.get(id=item_id)
        return render(request, 'library/learning_object.html', {'item':item})

    except models.LearningObject.DoesNotExist:
        raise Http404
