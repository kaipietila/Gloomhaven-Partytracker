from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import forms
from .models import Party, Character


@login_required
def view_core(request):
    user_partys = []
    all_partys = Party.objects.all().order_by('name')
    all_characters = Character.objects.all()
    for party in all_partys:
        if party.creator == request.user:
            user_partys.append(party)
    return render(request, 'core/overview.html', {'user_partys': user_partys, 'all_characters': all_characters})


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
