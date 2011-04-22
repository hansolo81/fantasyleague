# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from fantasyleague.teammanagement.models import *
from fantasyleague.teammanagement.forms import *
from fantasyleague.base.models import *
from fantasyleague.league.models import *
from fantasyleague.league.forms import JoinLeagueForm, CreateLeagueForm
from django.http import HttpResponseRedirect
import hashlib, random


@login_required(redirect_field_name='redirect_to')
def show_league(request, league_id):
    league = League.objects.get(id=league_id)
    league_teams = list(LeagueTeam.objects.filter(league=league))
    myTeam = MyTeam.objects.get(user=request.user)
    league_teams.sort(reverse=True)

    fixtureslist = Fixture.objects.filter(game_week__id=1)
    return render_to_response('league/private_league.html', {'league_teams': league_teams, 'league': league, 'fixtureslist': fixtureslist, 'myTeam': myTeam}, context_instance=RequestContext(request))


@login_required(redirect_field_name='redirect_to')
def show_leagues(request):
    myTeam = MyTeam.objects.get(user=request.user)
    leagueTeam = LeagueTeam.objects.filter(team=myTeam)
    leagues = League.objects.filter(leagueteam=leagueTeam)
    if not leagues:
        return HttpResponseRedirect("/league/join_league")
    fixtureslist = Fixture.objects.filter(game_week__id=1)
    return render_to_response('league/my_leagues.html', {'leagues': leagues, 'fixtureslist': fixtureslist, 'myTeam': myTeam}, context_instance=RequestContext(request))


@login_required(redirect_field_name='redirect_to')
def show_join_league(request):
    form = JoinLeagueForm()
    fixtureslist = Fixture.objects.filter(game_week__id=1)  
    if request.method == 'POST':        
        form = JoinLeagueForm(request.POST)
        if form.is_valid():  
            league = League.objects.get(code=form['leagueCode'].data)
            myTeam = MyTeam.objects.get(user=request.user)
            if LeagueTeam.objects.filter(league=league, team=myTeam):
                return render_to_response('league/join_league.html', {'fixtureslist': fixtureslist, 'form': form, 'error': 'You are already registered in the league %s' % league}, context_instance=RequestContext(request))                
            
            league_team = LeagueTeam()
            league_team.league = league
            league_team.team =  myTeam
            league_team.save()
            return HttpResponseRedirect("/league/leagues")
        else:
            return ''
    return render_to_response('league/join_league.html', {'fixtureslist': fixtureslist, 'form': form}, context_instance=RequestContext(request))
    

@login_required(redirect_field_name='redirect_to')
def show_create_league(request):
    form = CreateLeagueForm()
    fixtureslist = Fixture.objects.filter(game_week__id=1)    
    if request.method == 'POST':        
        form = CreateLeagueForm(request.POST)
        if form.is_valid():
            salt = hashlib.md5(str(random.random())).hexdigest()[:8]
            league = League()
            league.name = form['leagueName'].data        
            league.user = request.user
            league.code = salt;
            league.save()   
            
            myTeam = MyTeam.objects.get(user=request.user)
            
            league_team = LeagueTeam()
            league_team.league = league
            league_team.team =  myTeam
            league_team.save()
                    
            return HttpResponseRedirect("/league/leagues")
    return render_to_response('league/create_league.html', {'fixtureslist': fixtureslist, 'form': form}, context_instance=RequestContext(request))


class CmpAttr:
    def __init__(self, attr):
        self.attr = attr
        
    def __call__(self, x, y):
        return cmp(getattr(x, self.attr), getattr(y, self.attr))
    
    