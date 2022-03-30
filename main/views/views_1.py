# views maps

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import MapsMarker


@csrf_exempt
def maps(request, *args, **kwarg):
    pointer = request.POST.get('points', None)
    if request.POST:
        pointer = pointer.replace('LatLng', '')
        insert = MapsMarker.objects.create(pointer=pointer)
        insert.save()
    return render(request, 'maps.html', {})
