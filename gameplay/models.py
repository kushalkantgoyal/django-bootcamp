from django.contrib.auth.models import User
from django.db import models

GAME_STATUS_COICES = (
    ('F', "First Player to Move"),
    ('S', "Second Player to Move"),
    ('W', "First Player Wins"),
    ('L', "Second Player Wins"),
    ('D', "Draw")
)


class Game(models.Model):
    first_player = models.ForeignKey(User, related_name="games_first_player", on_delete=models.PROTECT)
    second_player = models.ForeignKey(User, related_name="games_second_player", on_delete=models.PROTECT)
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='F', choices=GAME_STATUS_COICES)

    def __str__(self):
        return "{0} vs {1}".format(
            self.first_player, self.second_player)

class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)
    by_first_player = models.BooleanField()

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
