import django_filters
from django_filters import ModelChoiceFilter
from .models import *

class PlayerFilter(django_filters.FilterSet):

    class Meta:
        model = Log
        fields = ['player_id']