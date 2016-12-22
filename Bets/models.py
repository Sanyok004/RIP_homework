from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models


class Team(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30, default='')
    sport = models.CharField(max_length=30, default='')
    country = models.CharField(max_length=30, default='')
    description = models.TextField(default='')
    coach = models.CharField(max_length=50, default='')
    win = models.IntegerField(default=0)
    games = models.IntegerField(default=0)
    logo = models.ImageField(upload_to='images/')
    user_bet = models.ManyToManyField(User, through='Bet', related_name='users')


class SportFilter(admin.SimpleListFilter):
    title = 'Sport'
    parameter_name = 'sport'

    def lookups(self, request, model_admin):
        return [
            ('Football', 'Футбольные клубы'),
            ('Hockey', 'Хоккейные клубы')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'Football':
            return queryset.filter(sport='Футбол')
        elif self.value() == 'Hockey':
            return queryset.filter(sport='Хоккей')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'games', 'win', 'percent_win')
    search_fields = ['name']
    list_filter = (SportFilter,)

    @staticmethod
    def percent_win(obj):
        return '{0:.1%}'.format(obj.win/obj.games)


class Bet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    ratio = models.FloatField(default=1)
    amount = models.IntegerField(default=0)
    date = models.DateField(auto_now=True)


class BetAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'ratio', 'amount', 'date')
