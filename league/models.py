from django.db import models
from django.contrib.auth.models import User
from fantasyleague.base.models import Player
from fantasyleague.teammanagement.models import *

# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User)
    code = models.CharField(max_length=20)
    
        
    def __unicode__(self):
        return self.name

class LeagueTeam(models.Model):
    league = models.ForeignKey(League)
    team = models.ForeignKey(MyTeam)

    def __unicode__(self):
        return '%s' % self.team
    
    
    def __cmp__(self, other):
        return cmp(self.total_points(), other.total_points())

    def total_points(self):
        try:
            total = 0
            myTeamPlayers = MyTeamPlayer.objects.filter(myTeam=self.team, is_first_eleven=True)

            for player in myTeamPlayers:
                total += player.player.total_points()
            return total
        except:
            return 'Exception encountered for %s' % self
