# views maps
from django.shortcuts import render


def views(request, *args, **kwarg):
    print('Views page')
    return render(request, 'views.html', {})
