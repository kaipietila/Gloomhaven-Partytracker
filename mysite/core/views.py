from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms

@login_required
def view_core(request):
    return render(request, 'core/home.html')


@login_required
def create_party(request):
    if request.method == 'POST':
        form = forms.CreatePartyForm(request.POST)
        if form.is_valid():
            party = form.save(commit=False)
            party.creator = request.user
            party.save()
            return redirect('core:home')
    else:
        form = forms.CreatePartyForm()
    return render(request, 'core/create_party.html', {'form':form})


@login_required
def create_character(request):
    if request.method == 'POST':
        form = forms.CreateCharForm(request.POST)
        if form.is_valid():
            char = form.save(commit=False)
            char.creator = request.user
            char.save()
            return redirect('core:home')
    else:
        form = forms.CreateCharForm()
    return render(request, 'core/create_character.html', {'form':form})
