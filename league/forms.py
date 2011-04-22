from django import forms
from fantasyleague.league.models import *
from fantasyleague.base.models import *


class JoinLeagueForm(forms.Form):
    leagueCode = forms.CharField(max_length=8, label="League Code")
    
    
class CreateLeagueForm(forms.Form):
    leagueName = forms.CharField(max_length=20, label="League Name")
    gameWeek = forms.ModelChoiceField(queryset=GameWeek.objects.all(), empty_label='---Select GameWeek---', label="Scoring Starts")  





