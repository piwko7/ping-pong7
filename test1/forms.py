from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import MatchScore, Table
import datetime


class MatchScoreForm(ModelForm):
    # winner = MatchScore(help_text='Use puns liberally')
    class Meta:
        model = MatchScore
        fields = ['winner', 'winner_sets', 'lost_sets', 'lost', 'duel_date']

    # def clean(self):
    #     cleaned_data = super().clean()
    #     duel_date = cleaned_data.get('duel_date')
    #     if duel_date is None:
    #         self.add_error('duel_date', " Nieprawidłowy format daty")
    #         raise ValidationError("Test")
    #     return cleaned_data

    def clean_duel_date(self):
        duel_date = self.cleaned_data.get('duel_date')
        if duel_date == None:
            raise ValidationError("Wrong format")
        return duel_date

    def clean_lost(self):
        winner = self.cleaned_data.get('winner')
        lost = self.cleaned_data.get('lost')
        if winner == lost:
            raise ValidationError("Zwycięzca i przegrany nie może być taki sam.")
        return lost

    def clean_winner_sets(self):
        winner_sets = self.cleaned_data.get('winner_sets')
        if winner_sets != 3:
            raise ValidationError("Zwycięzca musi mieć 3 sety")
        return winner_sets

    def clean_lost_sets(self):
        lost_sets = self.cleaned_data.get('lost_sets')
        if lost_sets == 3:
            raise ValidationError("Przegrany nie może mieć 3 setów")
        return lost_sets


    # def clean(self):
    #     cleaned_data = super().clean()
    #     duel_date = cleaned_data.get('duel_date')
    #     print(duel_date)
    #     if cleaned_data.get('winner') == cleaned_data.get('lost'):
    #         raise ValidationError("The Winner and Loser cannot be the same.")
    #     if cleaned_data.get('winner_sets') != 3:
    #         raise ValidationError("Winner must have 3 sets !")
    #     if cleaned_data.get('lost_sets') == 3:
    #         raise ValidationError("The losing player cannot have 3 sets!")
    #     if duel_date == None:
    #         raise ValidationError("Tpppppppppppp!")
    #     return cleaned_data


class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = ['player', 'matches', 'number_of_wins', 'number_of_lost', 'points', 'won_sets', 'lost_sets', 'set_ratio']

