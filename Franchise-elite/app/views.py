"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from .forms import *
from .models import *
from .tables import *
from .filters import PlayerFilter
from django.views.generic import ListView, DetailView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.db.models import Avg, Count, Min, Sum
from django.db.models.functions import Cast
from django.db.models import FloatField

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )
def profile(request):
    template = 'profile.html'
    table = PlayerTable(Log.objects.all().aggregate)
    context = {'objectlist': Player.objects.all(),
               'table': table}

    return render(request, template, context)

class LogList(FilterView):
    model = Log
    context_object_name = 'logs'
    filter_class = PlayerFilter

def player_list(request):
    f = PlayerFilter(request.GET, queryset=Log.objects.all())
    agg = PlayerFilter(request.GET, queryset=Log.objects.values('player_id').annotate(total_score=Sum('score'),
                                                                                      total_made=Sum('fldGoalMade'),
                                                                                      total_att=Sum('fldGoalAtt'),
                                                                                      fg_percent=(Sum('fldGoalMade')/Sum('fldGoalAtt'))*100,
                                                                                      total_three_made=Sum('threePtMade'),
                                                                                      total_three_att=Sum('threePtAtt'),
                                                                                      three_pt_percent=(Sum('threePtMade')/Sum('threePtAtt'))*100,
                                                                                      total_reb=Sum('rebound'),
                                                                                      total_off_reb=Sum('offRebound'),
                                                                                      total_def_reb=Sum('defRebound'),
                                                                                      total_pfouls=Sum('pFouls'),
                                                                                      total_steals=Sum('steals'),
                                                                                      total_turnovers=Sum('turnovers'),
                                                                                      total_blocks=Sum('blocks'),
                                                                                      total_assists=Sum('assist')
                                                                                      ))
    #photo_filter = Log.objects.filter(player_id='player_id').values_list('player__photo')
    return render(request, 'profile.html', {'filter': f, 'agg_filter': agg})

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def add_school(request):
    template = 'add_school.html'

    if request.method == 'POST':
        form=SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_school')
    return render(request,template, {
        'form': SchoolForm(),
        })

def add_game(request):
    template = 'add_game.html'

    if request.method == 'POST':
        form=GameForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_game')
    return render(request,template, {
        'form': GameForm(),
        })

def add_player(request):
    template = 'add_player.html'

    if request.method == 'POST':
        form=PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_player')
    return render(request,template, {
        'form': PlayerForm(),
        })

def add_position(request):
    template = 'add_position.html'

    if request.method == 'POST':
        form=PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_position')
    return render(request,template, {
        'form': PositionForm(),
        })

def add_team(request):
    template = 'add_team.html'

    if request.method == 'POST':
        form=PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_team')
    return render(request,template, {
        'form': TeamForm(),
        })

def add_log(request):
    template = 'add_log.html'

    if request.method == 'POST':
        form=PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_log')
    return render(request,template, {
        'form': LogForm(),
        })