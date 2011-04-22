from django import forms
from fantasyleague.base.models import *

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team

    class Media:
        js = ('/media/green-web-hosting/js/jquery.js',)
        css = ('/media/green-web-hosting/css/style.css',)


class PlayerStatsForm(forms.Form):
    player = forms.ModelChoiceField(queryset=Player.objects.all(),empty_label=None)
    #player.widget.attrs["onchange"] = " refreshpage(this.value)"

    class Media:
        js = ('/media/green-web-hosting/js/jquery.js',)
        css = ('/media/green-web-hosting/css/style.css',)



class PositionForm(forms.Form):
    position = forms.ModelChoiceField(queryset=Position.objects.all(), empty_label=None)


class TeamForm(forms.Form):
    position = forms.ModelChoiceField(queryset=Team.objects.all().order_by('name'), empty_label=None)

