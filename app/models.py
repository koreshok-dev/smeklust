"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Question(models.Model):
    date_added=models.DateTimeField(auto_now_add=True)
    text=models.TextField()
    def __str__(self):
        return self.text
class Game(models.Model):
    date_added=models.DateTimeField(auto_now_add=True)
    n_questions=models.IntegerField()
    q1=models.IntegerField(null=True)
    q2=models.IntegerField(null=True)
    q3=models.IntegerField(null=True)
    q4=models.IntegerField(null=True)
    q5=models.IntegerField(null=True)
    q6=models.IntegerField(null=True)
    q7=models.IntegerField(null=True)
    q8=models.IntegerField(null=True)
    q9=models.IntegerField(null=True)
    q10=models.IntegerField(null=True)
    q11=models.IntegerField(null=True)
    q12=models.IntegerField(null=True)
    q13=models.IntegerField(null=True)
    q14=models.IntegerField(null=True)
    q15=models.IntegerField(null=True)
    def __str__(self):
        return str(self.id)+str(self.date_added)

class Lobby(models.Model):
    player1=models.IntegerField()
    player2=models.IntegerField(null=True)
    player3=models.IntegerField(null=True)
    player4=models.IntegerField(null=True)
    player5=models.IntegerField(null=True)
    player6=models.IntegerField(null=True)
    is_active=models.BooleanField()
    n_players=models.IntegerField()
    game=models.ForeignKey(Game, on_delete=models.PROTECT)
    voted=models.IntegerField(default=0)

class Answer(models.Model):
    lobby=models.ForeignKey(Lobby,on_delete=models.PROTECT)
    player1=models.IntegerField()
    player2=models.IntegerField()
    question=models.ForeignKey(Question, on_delete=models.PROTECT)
    answ1=models.TextField(null=True)
    answ2=models.TextField(null=True)
    score1=models.IntegerField(default=0)
    score2=models.IntegerField(default=0)


    
    
