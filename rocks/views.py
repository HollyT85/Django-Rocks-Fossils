from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from .models import Rock

def all_rocks(request):
    # View all rocks on the rock page
    rocks = Rock.objects.all()

    context = {
        'rocks': rocks,
    }

    return render(request, 'rocks/rocks.html', context)

# @login_required
# def add_rock(request):
#     if not request.user.is_superuser:
#         messages.error(request, 'You are not authorised to do this.')
#         return redirect(reverse('home'))

    
