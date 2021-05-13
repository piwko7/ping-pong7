from django.shortcuts import render, get_object_or_404, redirect

from .forms import MatchScoreForm, TableForm
from .models import MatchScore, Table

from django.contrib import messages


# Create your views here.
def main_view(request):
    return render(request, 'index.html')


def all_scores(request):
    match = MatchScore.objects.order_by('-duel_date')
    return render(request, 'pingpong.html', {'form': match})

def new_score(request):
    form = MatchScoreForm(request.POST or None)

    if form.is_valid():


        winner_name = form.cleaned_data.get('winner')
        winnser_sets = form.cleaned_data.get('winner_sets')
        lost_sets = form.cleaned_data.get('lost_sets')
        lost_name = form.cleaned_data.get('lost')
        points = winnser_sets - lost_sets
        if points >= 2:
            winner_points = 3
            lost_points = 0
        else:
            winner_points = 2
            lost_points = 1


        winner = Table.objects.get(player=winner_name)
        matches_1 = winner.matches + 1
        number_of_wins_1 = winner.number_of_wins + 1
        number_of_lost_1 = winner.number_of_lost
        points_1 = winner.points + winner_points
        won_sets_1 = winner.won_sets + winnser_sets
        lost_sets_1 = winner.lost_sets + lost_sets
        set_ratio_1 = winner.set_ratio + (winnser_sets - lost_sets)
        Table.objects.filter(player=winner_name).update(matches=matches_1, number_of_wins=number_of_wins_1,
                                                        points=points_1, won_sets=won_sets_1, lost_sets=lost_sets_1,
                                                        set_ratio=set_ratio_1)

        lost = Table.objects.get(player=lost_name)
        matches_2 = lost.matches + 1
        number_of_wins_2 = lost.number_of_wins
        number_of_lost_2 = lost.number_of_lost + 1
        points_2 = lost.points + lost_points
        won_sets_2 = lost.won_sets + lost_sets
        lost_sets_2 = lost.lost_sets + winnser_sets
        set_ratio_2 = lost.set_ratio + (lost_sets - winnser_sets)
        Table.objects.filter(player=lost_name).update(matches=matches_2, number_of_lost=number_of_lost_2,
                                                      points=points_2, won_sets=won_sets_2, lost_sets=lost_sets_2,
                                                      set_ratio=set_ratio_2)

        form.save()
        return redirect(all_scores)
    return render(request, 'match_form.html', {'form': form})

def edit_score(request, id):
    match = get_object_or_404(MatchScore, pk=id)
    form = MatchScoreForm(request.POST or None, instance=match)

    if form.is_valid():
        form.save()
        return redirect(all_scores)
    return render(request, 'match_form.html', {'form': form})

def delete_score(request, id):
    match = get_object_or_404(MatchScore, pk=id)
    if request.method == 'POST':
        match.delete()
        return render(all_scores)

    return render(request, 'confirm.html', {'form': match})

def table_results(request):
    match = MatchScore.objects.order_by('-duel_date')
    gracze = []
    for m in match:
        if m.winner not in gracze:
            gracze.append(m.winner)
        if m.lost not in gracze:
            gracze.append(m.lost)

    tabela = []
    for g in gracze:
        zwyciestwa = len([m for m in match if m.winner == g])
        przegrane = len([m for m in match if m.lost == g])
        mecze = zwyciestwa + przegrane
        tabela.append({'gracz': g, 'mecze': mecze, 'zwyciestwa': zwyciestwa, 'przegrane': przegrane})
    return render(request, 'table.html', {'form': tabela})

def show_table(request):
    table = Table.objects.all()
    return render(request, 'show_table.html', {'table': table})

def under(request):
    return render(request, 'under.html')