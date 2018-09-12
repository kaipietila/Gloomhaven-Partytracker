from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def view_core(request):
    return render(request, 'core/home.html')


@login_required
def view_party(request):
    return render(request, 'core/party.html')


@login_required
def create_party(request):
    return render(request, 'core/create_party.html')


@login_required
def create_character(request):
    return render(request, 'core/create_character.html')


