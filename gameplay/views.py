from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


# Create your views here.
from gameplay.forms import MoveForm
from gameplay.models import Game


@login_required
def game_detail(request, id):
    game = get_object_or_404(Game, pk=id)
    context = {'game': game}
    if game.is_users_move(request.user):
        context['form'] = MoveForm()
    return render(request, "gameplay/game_detail.html", context)