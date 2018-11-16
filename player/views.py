from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from gameplay.models import Game
from player.forms import InvitationForm


@login_required
def home(request):
    my_games = Game.objects.games_of_user(request.user)
    active_games = my_games.active()

    return render(request, "player/home.html",
                  {'games': active_games})

@login_required
def new_invitation(request):
    form = InvitationForm()
    return render(request, "player/new_invitation_form.html", {'form' : form})