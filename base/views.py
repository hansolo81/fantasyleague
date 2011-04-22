from django.shortcuts import render_to_response, get_object_or_404
from fantasyleague.base.models import Team, Player, PlayerStats, ValueRange
from fantasyleague.base.forms import PlayerStatsForm
from django.template import RequestContext
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(redirect_field_name='redirect_to')
def teams_list(request):
    teams_list = Team.objects.all().order_by('name')
    return render_to_response('base/teams_list.html', {'teams_list': teams_list})


@login_required(redirect_field_name='redirect_to')
def players_list(request, position_id=None, team_id=-1, value_id=-1):
    #if request.is_ajax():
    errorstage = 0;
    try:
        players_list = Player.objects.order_by('position', '-value')
        if position_id != '-1':
            players_list = players_list.filter(position__id=position_id)
        if team_id != '-1':
            players_list = players_list.filter(team__id=team_id)
        if value_id != '-1':
            valueObj = ValueRange.objects.get(id=value_id)
            players_list = players_list.filter(value__gt=valueObj.minValue, value__lt=valueObj.maxValue)
        data = serializers.serialize('json', players_list, indent=4, relations=('position', 'team'), extras=('__unicode__','total_points', 'current_team_code'))
        return HttpResponse(data, 'application/javascript')
    except:
        return HttpResponse(errorstage)
    #else:
        #return render_to_response('base/players_list.html', {'players_list': players_list})


@login_required(redirect_field_name='redirect_to')
def player_stats(request, player_id):
    form = PlayerStatsForm(initial={'player': player_id})
    players_list = Player.objects.all().order_by('firstname')
    player = Player.objects.get(id=player_id)
    player_stats = list(PlayerStats.objects.filter(player=player))
    dict = {'players_list': players_list, 'player': player, 'player_stats': player_stats}
    return render_to_response('base/player_stats.html', {'dict': dict, 'form': form}, context_instance=RequestContext(request))


@login_required(redirect_field_name='redirect_to')
def player_details(request, player_id):
    errorstage = 0;
    try:
        player = Player.objects.filter(id=player_id)
        data = serializers.serialize('json', player, indent=4, relations=('position', 'team'), extras=('__unicode__','total_points', 'current_team'))
        return HttpResponse(data, 'application/javascript')
    except:
        return HttpResponse(player)

