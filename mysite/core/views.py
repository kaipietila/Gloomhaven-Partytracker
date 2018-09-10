from django.shortcuts import render


def view_core(request):
    return render(request, 'core/home.html')


def view_party(request):
    return render(request, 'core/party.html')