from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from fantasyleague.teammanagement.models import *

def logout_view(request):
    logout(request)


def log_me_in(request):
    try:
        myTeam = MyTeam.objects.get(user=request.user)
    except:
        return HttpResponseRedirect("/teammanagement/firsttime/")
    myTeamPlayers = MyTeamPlayer.objects.filter(myTeam=myTeam)

    if myTeam and myTeamPlayers:
        return HttpResponseRedirect("/teammanagement/transfers/")
    else:
        return HttpResponseRedirect("/teammanagement/firsttime/")


