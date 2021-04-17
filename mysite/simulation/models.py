from django.db import models

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length= 200)
    #need all the team attributes

class Player(models.Model):
    player_name = models.CharField(max_length= 50)
    #need all the player attributes 

class User(models.Model):
    user_name = models.CharField(max_length= 50)
    