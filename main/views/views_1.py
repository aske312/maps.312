# views maps
from django.shortcuts import render


def maps(request, *args, **kwarg):
    print('Welcome page')
    return render(request, 'maps.html', {})
