from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Rock
from users.models import Profile
from .forms import RockForm

def all_rocks(request):
    # View all rocks on the rock page
    rocks = Rock.objects.all()
    # rock_fossil = None


    # if request.GET:
    #     if 'rock_fossil' in request.GET:
    #         item = request.GET['rock_fossil'].split(',')
    #         rock_fossil = rocks.filter(rocks__rock_fossil__in=item)
    #         rock = Rocks.objects.filter(rock_fossil__in=item)

    context = {
        'rocks': rocks,
        # 'rock_fossil': rock_fossil
    }

    return render(request, 'rocks/rocks.html', context)


def rock_info(request, rock_id):
    # Get individual rock/fossil info
    rock = get_object_or_404(Rock, pk=rock_id)

    context = {
        'rock': rock,
    }

    return render(request, 'rocks/rock-info.html', context)



@login_required
def add_rock(request):
    
    if not request.user.is_authenticated:

        return redirect(reverse('home'))
    
    if request.method == 'POST':
        rock_form = RockForm(request.POST, request.FILES)
        if rock_form.is_valid():
            rock = rock_form.save(commit=False)
            rock.owner = request.user
            rock = rock_form.save()
            return redirect(reverse('rock_info', args=[rock.id]))

    else:
        rock_form = RockForm()

    template = 'rocks/add_rock.html'
    context = {
        'rock_form': rock_form,
    }

    return render(request, template, context)

@login_required()
def edit_rock(request, rock_id):

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    rock = get_object_or_404(Rock, pk=rock_id)

    if request.method == 'POST':
        rock_form = RockForm(request.POST, request.FILES, instance=rock)
        if rock_form.is_valid():
            rock_form.save()
            return redirect(reverse('rock_info', args=[rock.id]))
        else:
            console.log('failed')
    else:
        rock_form = RockForm(instance=rock)

    template = 'rocks/edit_rock.html'
    context = {
        'rock_form': rock_form,
        'rock': rock
    }

    return render(request, template, context)