from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def login_view(request):
    """
    login page
    """
    return render(request, 'accounts/login.html')


def signup_view(request):
    """
    signup page, for new users
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
