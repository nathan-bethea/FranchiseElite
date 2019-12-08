"""
Definition of models.
"""

from django.db import models
import django_filters


class Team(models.Model):
    team_name = models.CharField(max_length = 256)
    coach = models.CharField(max_length = 256)

    def __str__(self):
        return self.team_name

class School(models.Model):
    school_name = models.CharField(max_length = 256)
    address = models.CharField(max_length = 256)
    city = models.CharField(max_length = 256)
    state = models.CharField(max_length = 256)
    zipcode = models.IntegerField()
   
    def __str__(self):
        return self.school_name

class Position(models.Model):
    position_name = models.CharField(max_length = 256)

    def __str__(self):
        return self.position_name

class Player(models.Model):
    player_id = models.IntegerField()
    team_id = models.ForeignKey(Team, on_delete = models.CASCADE)
    jersey_num = models.IntegerField()
    pos_num = models.ForeignKey(Position, on_delete = models.CASCADE)
    school_id = models.ForeignKey(School, on_delete = models.CASCADE)
    fname = models.CharField(max_length = 256)
    lname = models.CharField(max_length = 256)
    dateOfbirth = models.DateField()
    height = models.DecimalField(decimal_places = 2, max_digits = 6)
    photo = models.ImageField(upload_to="gallery", default = 'noImageAttached.png')

    def __str__(self):
        return self.fname + " " + self.lname

class Game_List(models.Model):
    game_id = models.IntegerField()
    game_date = models.DateField()
    team_id = models.ForeignKey(Team, on_delete = models.CASCADE)
    home_adv = models.BooleanField()
    win = models.BooleanField()
    score = models.IntegerField()
    o_score = models.IntegerField()

    def __str__(self):
        return "Game "+str(self.game_id)+" "+str(self.game_date)

class Log(models.Model):
    log_id = models.IntegerField()
    game_id = models.ForeignKey(Game_List, on_delete = models.CASCADE)
    player_id = models.ForeignKey(Player, on_delete = models.CASCADE)
    score = models.IntegerField()
    time_played = models.DateTimeField()
    fldGoalMade = models.FloatField()
    fldGoalAtt = models.FloatField()
    threePtMade = models.FloatField()
    threePtAtt = models.FloatField()
    rebound = models.IntegerField()
    offRebound = models.IntegerField()
    defRebound = models.IntegerField()
    pFouls = models.IntegerField()
    steals = models.IntegerField()
    turnovers = models.IntegerField()
    blocks = models.IntegerField()
    assist = models.IntegerField()
