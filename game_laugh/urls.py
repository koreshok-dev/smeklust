"""
Definition of urls for game_laugh.
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
    #path('lobby',views.create_lobby,name='create_lobby'),
    path('clobby/?P<n_players>d)/',views.create_lobby,name='create_lobby'),
    path('slobby/?P<lobby_number>d)/',views.show_lobby,name='show_lobby'),
    path('lobby_list/',views.lobby_list,name='lobby_list'),
    path('lobby_join/?P<lobby_number>d)?P<n_connected>d)/',views.lobby_join,name='lobby_join'),
    path('game/?P<lobby_id>d',views.start_game,name='start_game'),
    path('waiting/?P<lobby_id>d',views.wait_answers,name='wait_answers'),
    path('wait_votes/?P<lobby_id>d',views.wait_votes,name='wait_votes'),
    path('rate_answers/?P<lobby_id>d',views.rate_answers,name='rate_answers'), 
    path('end_game/?P<lobby_id>d',views.end_game,name='end_game'),
    path('admin/', admin.site.urls),
]
