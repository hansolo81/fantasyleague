# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from fantasyleague.teammanagement.models import *
from fantasyleague.teammanagement.forms import *
from fantasyleague.base.models import *
from fantasyleague.base.forms import TeamForm
from django.http import HttpResponseRedirect

@login_required(redirect_field_name='redirect_to')
def show_myteam_transfers(request, redirect_url='teammanagement/transfers.html', form_class=TransfersForm):
    myTeam = None
    error = None
    try:
        myTeam = MyTeam.objects.get(user=request.user)
    except:
        pass

    if request.method == 'POST':
        form = form_class(request.POST)
        player_ids = request.POST.getlist("playerId")
        
        if form.is_valid() and not myTeam:
            teamName = form['teamName'].data
            myTeam = MyTeam()
            myTeam.user = request.user
            if teamName is not None:
                myTeam.name = teamName
            myTeam.save()


        playersToRemove = list(MyTeamPlayer.objects.filter(myTeam=myTeam))
        countgk = 0
        countdf = 0
        countmf = 0
        countfw = 0

        for pid in player_ids:
            thePlayer = Player.objects.get(id=pid)

            try:
                myTeamPlayer = MyTeamPlayer.objects.get(player=thePlayer)
                playersToRemove.remove(myTeamPlayer)
            except:
                myTeamPlayer = MyTeamPlayer()
                myTeamPlayer.myTeam = myTeam
                myTeamPlayer.player = thePlayer
                myTeamPlayer.transfer_week = 1

                try:
                    if thePlayer.position.code == 'GK':
                        if countgk == 1:
                            myTeamPlayer.is_first_eleven = 0
                        else:
                            myTeamPlayer.is_first_eleven = 1
                            countgk += 1
                    elif thePlayer.position.code == 'DF':
                        if countdf == 4:
                            myTeamPlayer.is_first_eleven = 0
                        else:
                            myTeamPlayer.is_first_eleven = 1
                            countdf += 1
                    elif thePlayer.position.code == 'MF':
                        if countmf == 4:
                            myTeamPlayer.is_first_eleven = 0
                        else:
                            myTeamPlayer.is_first_eleven = 1
                            countmf += 1
                    elif thePlayer.position.code == 'FW':
                        if countfw == 2:
                            myTeamPlayer.is_first_eleven = 0
                        else:
                            myTeamPlayer.is_first_eleven = 1
                            countfw += 1
                except:
                    return render_to_response(redirect_url, {'players_list': players_list,})
                myTeamPlayer.save()

        for player in playersToRemove:
            player.delete()
            
        if redirect_url == 'teammanagement/firsttimepick.html':   
            return HttpResponseRedirect("/teammanagement/myteam/")
    else:
        form = form_class()

    g = MyTeamPlayer.objects.filter(myTeam=myTeam, player__position__code='GK')
    d = MyTeamPlayer.objects.filter(myTeam=myTeam, player__position__code='DF')
    m = MyTeamPlayer.objects.filter(myTeam=myTeam, player__position__code='MF')
    f = MyTeamPlayer.objects.filter(myTeam=myTeam, player__position__code='FW')


    myplayers = {'g': g, 'd': d, 'm': m, 'f': f }

    fixtureslist = Fixture.objects.filter(game_week__id=1)

    players_list = Player.objects.all().order_by('position', '-value')

    return render_to_response(redirect_url, {'players_list': players_list, 'myplayers': myplayers, 'myTeam': myTeam, 'fixtureslist': fixtureslist, 'form': form, 'error':error}, context_instance=RequestContext(request))


@login_required(redirect_field_name='redirect_to')
def show_myteam(request):
    form = MyTeamForm(**{'user':request.user})
    myTeam = MyTeam.objects.get(user=request.user)
    g = __construct_list(myTeam, True, 'GK')
    d = __construct_list(myTeam, True, 'DF')
    m = __construct_list(myTeam, True, 'MF')
    f = __construct_list(myTeam, True, 'FW')
    r = __construct_list(myTeam, False)

    myplayers = {'g': g, 'd': d, 'm': m, 'f': f , 'r': r}

    fixtureslist = Fixture.objects.filter(game_week__id=1)

    return render_to_response('teammanagement/myteam.html', {'myplayers': myplayers, 'form': form, 'fixtureslist': fixtureslist, 'myTeam': myTeam},  context_instance=RequestContext(request))


def show_myteam_profile(request):
    form = MyTeamProfileForm()
    return render_to_response('teammanagement/myteamprofile.html', {'form': form },  context_instance=RequestContext(request))


def show_transfers(request, redirect_url='teammanagement/transfers.html'):
    return show_myteam_transfers(request, 'teammanagement/firsttimepick.html')


def show_firsttime(request):
    return show_myteam_transfers(request, 'teammanagement/firsttimepick.html', FirstTimeTransferForm)


def __construct_list(myTeam, is_first_eleven=True, position_code=None):
    players_list = MyTeamPlayer.objects.filter(myTeam=myTeam, is_first_eleven=is_first_eleven)
    if position_code is not None:
        players_list = players_list.filter(player__position__code=position_code)
    players_list = list(players_list)
    if position_code is not None:
        if len(players_list) == 1:
            players_list.insert(0,None)
            players_list.insert(1,None)
            players_list.insert(3,None)
            players_list.insert(4,None)
        if len(players_list) == 2:
            players_list.insert(0,None)
            players_list.insert(2,None)
            players_list.insert(4,None)
        if len(players_list) == 3:
            players_list.insert(0,None)
            players_list.insert(4,None)
        elif len(players_list) == 4:
            players_list.insert(2,None)
    return players_list
