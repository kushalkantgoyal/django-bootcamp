from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from gameplay.models import Game
from player.forms import InvitationForm
from player.models import Invitation


@login_required
def home(request):
    my_games = Game.objects.games_of_user(request.user)
    active_games = my_games.active()

    return render(request, "player/home.html",
                  {'games': active_games})

@login_required
def new_invitation(request):
    if request.method == "POST":
        invitation = Invitation(from_user= request.user)
        form = InvitationForm(instance=invitation, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("player_home")
    else:
        form = InvitationForm()
        return render(request, "player/new_invitation_form.html", {'form' : form})