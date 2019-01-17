from django.shortcuts import render


def index(request):
    return render(request, 'journal/home.html')


#TODO create a entry-view and then show all entries on index page
