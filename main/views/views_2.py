# views result

from django.shortcuts import render
from .models import MapsMarker


def views(request, *args, **kwarg):
    pointers = MapsMarker.objects.all()
    return render(request, 'views.html', {'pointers': pointers})
