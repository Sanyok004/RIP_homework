from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from Bets.forms import AuthForm, RegistrationForm


@login_required(login_url='/auth/')
def main(request):
    return render(request, 'teams.html')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def authorization(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data.get('username'), password=data.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = AuthForm()
    return render(request, 'auth.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/auth/')
