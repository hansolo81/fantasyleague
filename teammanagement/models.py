from django.db import models
from django.contrib.auth.models import User
from fantasyleague.base.models import Player

# Create your models here.

class MyTeam(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class MyTeamPlayer(models.Model):
    myTeam = models.ForeignKey(MyTeam)
    player = models.ForeignKey(Player)
    transfer_week = models.IntegerField()
    is_first_eleven = models.BooleanField()

    def __unicode__(self):
        return '%s' % self.player

