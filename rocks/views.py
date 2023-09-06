from django.shortcuts import render

from .models import Rock

def all_rocks(request):
    # View all rocks on the rock page
    rocks = Rock.objects.all()

    context = {
        'rocks': rocks,
    }

    return render(request, 'rocks/rocks.html', context)

