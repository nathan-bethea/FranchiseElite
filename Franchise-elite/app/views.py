"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from .forms import *

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