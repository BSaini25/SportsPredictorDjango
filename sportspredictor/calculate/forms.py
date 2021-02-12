from django import forms 
from django.core.exceptions import ValidationError


class InputForm(forms.Form): 
    league = forms.CharField(max_length = 50)
    away_team = forms.CharField(max_length = 50) 
    home_team = forms.CharField(max_length = 50)

    def clean_league(self):
        data = self.cleaned_data['league']

        if data.isnumeric():
            raise ValidationError(_('Invalid league'))

        return data

    def clean_away_team(self):
        data = self.cleaned_data['away_team']

        if data.isnumeric():
            raise ValidationError(_('Invalid team'))

        return data

    def clean_home_team(self):
        data = self.cleaned_data['home_team']

        if data.isnumeric():
            raise ValidationError(_('Invalid team'))

        return data
