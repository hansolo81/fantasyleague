from django import forms
from fantasyleague.teammanagement.models import *
from fantasyleague.base.models import *


class MyTeamForm(forms.Form):
    captain = forms.ModelChoiceField(queryset=MyTeamPlayer.objects.none(), empty_label='---Select Captain---')    
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(forms.Form, self).__init__(*args, **kwargs)
        myTeam = MyTeam.objects.get(user=self.user)
        self.fields['captain'].queryset = MyTeamPlayer.objects.filter(myTeam=myTeam, is_first_eleven=True)        
    

    class Media:
        js = ('http://localhost:8000/sitemedia/js/myteam.js',)


class TransfersForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Team.objects.all(), empty_label='---Any Team---', required=False)
    value = forms.ModelChoiceField(queryset=ValueRange.objects.all(), empty_label='---Any Value---', required=False)

    class Media:
        js = ('http://localhost:8000/sitemedia/js/transfers.js',)


class FirstTimeTransferForm(TransfersForm):
    teamName = forms.CharField(max_length=100, label="Team Name")