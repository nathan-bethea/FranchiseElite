"""
Definition of forms.
"""

from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'

class GameForm(forms.ModelForm):
    class Meta:
        model = Game_List
        fields = '__all__'
    
class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = '__all__'

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = '__all__'

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = '__all__'