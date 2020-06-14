from django.urls import path
from django.http import HttpResponse
from counter.models import Counter


def counter(request):
    instance, created = Counter.objects.get_or_create(id=1)
    instance.value += 1
    instance.save()
    return HttpResponse(
        f'<div id="counter">{instance.value}</div>'
    )


urlpatterns = [
    path('', counter)
]
