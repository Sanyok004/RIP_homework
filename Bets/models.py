from django.contrib import admin
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


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'games', 'win', 'percent_win')
    search_fields = ['name']

    @staticmethod
    def percent_win(obj):
        return '{0:.1%}'.format(obj.win/obj.games)
