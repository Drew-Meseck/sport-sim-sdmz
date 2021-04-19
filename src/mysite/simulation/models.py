from django.db import models

# Create your models here.
class Team(models.Model):
    team_id         = models.BigAutoField(primary_key= True)
    team_name       = models.TextField()
    team_location   = models.TextField()
    stadium         = models.TextField()
    sponsored       = models.BooleanField(default= False)
    cap_space       = models.IntegerField()
    capital         = models.IntegerField()
    #need all the team attributes

class Player(models.Model):
    player_id = models.BigAutoField(primary_key= True)
    player_name = models.TextField()
    #need all the player attributes 

class User(models.Model):
    user_name = models.TextField()
    pass_word = models.TextField()
    team_id = models.ForeignKey(Team, on_delete= models.CASCADE)

class Trade(models.Model):
    pass

class Stat(models.Model):
    pass


