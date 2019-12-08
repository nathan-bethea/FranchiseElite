from django.contrib.auth import get_user_model
from django.db import models
import django_tables2 as tables
from .models import *
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import *

class PlayerTable(tables.Table):
    class Meta:
        model = Log
        template_name = "django_tables2/bootstrap-responsive.html"

class FilteredPlayerListView(SingleTableMixin, FilterView):
    table_class = PlayerTable
    model = Log
    template_name = "django_tables2/bootstrap-responsive.html"

    filterset_class = PlayerFilter
