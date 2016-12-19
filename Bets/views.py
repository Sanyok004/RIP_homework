from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from Bets.forms import AuthForm, RegistrationForm
from Bets.models import Team


@login_required(login_url='/auth/')
def main(request):
    return HttpResponseRedirect('/teams/')


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


class TeamsView(View):
    def get(self, request):
        teams = Team.objects.all()
        return render(request, 'teams.html', {'teams': teams, 'user': request.user.get_full_name()})


class TeamView(View):
    def get(self, request, id):
        team = Team.objects.filter(id__exact=id)[0]
        return render(request, 'team.html', {'team': team, 'user': request.user.get_full_name()})


def add_team(request):
    if request.method == 'POST':
        team = Team()
        team.logo = request.FILES.get('logo')
        team.name = request.POST.get('name')
        team.sport = request.POST.get('sport')
        team.country = request.POST.get('country')
        team.coach = request.POST.get('coach')
        team.games = request.POST.get('games')
        team.win = request.POST.get('win')
        team.description = request.POST.get('description')
        team.save()
        return HttpResponseRedirect('/team/{0}'.format(team.id))
    return HttpResponseRedirect('/')

