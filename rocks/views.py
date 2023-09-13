from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Rock

def all_rocks(request):
    # View all rocks on the rock page
    rocks = Rock.objects.all()

    context = {
        'rocks': rocks,
    }

    return render(request, 'rocks/rocks.html', context)


def rock_info(request, rock_id):
    # Get individual rock/fossil info
    rock = get_object_or_404(Rock, pk=rock_id)

    context = {
        'rock': rock,
    }

    return render(request, 'rocks/rock-info.html', context)



# @login_required
# def add_rock(request):
#     if not request.user.is_superuser:
#         messages.error(request, 'You are not authorised to do this.')
#         return redirect(reverse('home'))

    
