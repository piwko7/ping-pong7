from django.db import models

# Create your models here.

from datetime import datetime
from django.db import models

# Create your models here.

players = (
    ('Mateuszex', 'Mateuszex'),
    ('Piwkief', 'Piwkief'),
    ('Młody', 'Młody'),
    ('Prezes', 'Prezes'),
    ('Bogusław', 'Bogusław'),

)

winner = ((0, 'Gracz1'), (1, 'Gracz2'))

number_of_sets = ((0, 0), (1, 1), (2, 2), (3, 3))



class MatchScore(models.Model):
    winner = models.CharField(max_length=15, choices=players, blank=False)
    lost = models.CharField(max_length=15, choices=players, blank=False)
    winner_sets = models.PositiveSmallIntegerField(choices=number_of_sets, blank=False)
    lost_sets = models.PositiveSmallIntegerField(choices=number_of_sets, blank=False)
    duel_date = models.DateTimeField(null=True, blank=False, default=datetime.now)

    def __str__(self):
        return self.winner + ' ' + str(self.winner_sets) + ' - ' + str(self.lost_sets) + ' ' +  self.lost


class Table(models.Model):
    player = models.CharField(max_length=15, choices=players, blank=False)
    matches = models.PositiveSmallIntegerField(blank=False)
    number_of_wins = models.PositiveSmallIntegerField(blank=False)
    number_of_lost = models.PositiveSmallIntegerField(blank=False)
    points = models.PositiveSmallIntegerField(blank=False)
    won_sets = models.PositiveSmallIntegerField(blank=False)
    lost_sets = models.PositiveSmallIntegerField(blank=False)
    set_ratio = models.SmallIntegerField(blank=False)

    # def __str__(self):
    #     return self.player
