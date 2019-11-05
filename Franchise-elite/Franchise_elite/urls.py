"""
Definition of urls for Franchise_elite.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('add_school/', views.add_school, name='add_school'),
    path('add_game/', views.add_game, name='add_game'),
    path('add_player/', views.add_player, name='add_player'),
    path('add_position/', views.add_position, name='add_position'),
    path('add_team/', views.add_team, name='add_team'),
    path('add_log/', views.add_log, name='add_log'),
]
