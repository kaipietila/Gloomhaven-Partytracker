from django.shortcuts import render


def view_core(request):
    return render(request, 'core/home.html')