from django.contrib import admin
from Bets import models

admin.site.register(models.Team, models.TeamAdmin)
