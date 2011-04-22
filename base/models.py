from django.db import models

# Create your models here.

class GameWeek(models.Model):
    week_no = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return 'GameWeek %d (%s)' % (self.week_no, self.start_date.strftime('%d %b'))

class Position(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.code


class Player(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    value = models.DecimalField('Value (in MYR)', max_digits = 10, decimal_places=2)
    position = models.ForeignKey(Position)
    #teams = models.ManyToManyField(Team, through='TeamPlayer')

    def __unicode__(self):
        return '%s %s' % (self.firstname, self.lastname)

    def total_points(self):
        try:
            stats =  PlayerStats.objects.filter(player=self)
            if stats is not None:
                total = 0
                for weekly_stats in stats:
                    total += weekly_stats.weekly_points()
                return total
            else:
                return 0
        except:
            return 'Exception encountered for %s' % self

    def current_team(self):
        try:
            teams = TeamPlayer.objects.filter(player=self).order_by('-id')
            return teams[0].team
        except:
            return 'NA'

    def current_team_code(self):
        try:
            teams = TeamPlayer.objects.filter(player=self).order_by('-id')
            return teams[0].team.codename
        except:
            return 'NA'


class Venue(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Team(models.Model):
    codename = models.CharField(max_length=3)
    name = models.CharField(max_length=200)
    home_ground = models.ForeignKey(Venue)
    players = models.ManyToManyField(Player, through='TeamPlayer')

    def __unicode__(self):
        return self.name


class TeamPlayer(models.Model):
    team = models.ForeignKey(Team)
    player = models.ForeignKey(Player)
    week_joined = models.ForeignKey(GameWeek, related_name='joined')
    week_departed = models.ForeignKey(GameWeek, related_name='departed')


class PlayerStats(models.Model):
    player = models.ForeignKey(Player)
    game_week = models.ForeignKey(GameWeek)
    goals = models.IntegerField()
    assists = models.IntegerField()
    conceded = models.IntegerField()
    saves = models.IntegerField()
    yellow_card = models.IntegerField()
    red_card = models.IntegerField()
    bonus = models.IntegerField()

    def weekly_points(self):
        points = 0
        if self.player.position.code == 'FW':
            if self.goals != 0:
                points += self.goals*4
            if self.assists != 0:
                points += self.assists*3
            if self.yellow_card != 0:
                points -= self.yellow_card*1
            if self.red_card != 0:
                points -= 2
        else:
            return 0
        return points


class Fixture(models.Model):
    game_week = models.ForeignKey(GameWeek)
    home_team = models.ForeignKey(Team, related_name='home')
    away_team = models.ForeignKey(Team, related_name='away')
    home_score = models.IntegerField(blank=True, null=True)
    away_score = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return '%s vs %s' % (self .home_team, self.away_team)


class FixtureScorer(models.Model):
    fixture = models.ForeignKey(Fixture)
    scorer = models.ForeignKey(Player, related_name='scorer')
    assister = models.ForeignKey(Player, related_name='assister', blank=True, null=True)
    is_own_goal = models.BooleanField(default=False)

    def __unicode__(self):
        return '%s - %s' % (self.scorer, self.assister)


class ValueRange(models.Model):
    minValue = models.IntegerField()
    maxValue = models.IntegerField()

    def __unicode__(self):
        return '%s - %s' % (self.minValue, self.maxValue)
