from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import forms
from .models import Party, Character


@login_required
def view_core(request):
    user_partys = []
    all_partys = Party.objects.all().order_by('name')
    for party in all_partys:
        if party.creator == request.user:
            user_partys.append(party)
    return render(request, 'core/overview.html', {'user_partys': user_partys})


def view_party(request, party_id):
    """core overview you can get to each parties own view"""
    try:
        party = Party.objects.get(pk = party_id)
        party_characters = Character.objects.filter(party_id = party.pk)
        characters = party_characters
    except:
        raise Http404("Party does not exist")
    return render(request, 'core/party_detail.html', {'characters':characters})


@login_required
def create_party(request):
    if request.method == 'POST':
        form = forms.CreatePartyForm(request.POST)
        if form.is_valid():
            party = form.save(commit=False)
            party.creator = request.user
            party.save()
            return redirect('core:overview')
    else:
        form = forms.CreatePartyForm()
    return render(request, 'core/create_party.html', {'form': form})


@login_required
def create_character(request):
    if request.method == 'POST':
        form = forms.CreateCharForm(request.POST)
        if form.is_valid():
            char = form.save(commit=False)
            char.creator = request.user
            char.save()
            return redirect('core:overview')
    else:
        form = forms.CreateCharForm()
    return render(request, 'core/create_character.html', {'form': form})


@login_required
def create_scenario(request):
    if request.method =='POST':
        form = forms.CreateScenarioForm(request.POST)
        if form.is_valid():
            completed_scenario = form.save(commit=False)
            completed_scenario.creator = request.user
            completed_scenario.save()
            return redirect('core:overview')
    else:
        form = forms.CreateScenarioForm()
    return render(request, 'core/create_scenario.html', {'form': form})
