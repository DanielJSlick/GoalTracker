"""
Definition of models.
"""

from django.db import models

class Goal(models.Model):
    goal_name = models.CharField(max_length=100)
    start_date = models.DateTimeField()

class Progress(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    progress_text = models.CharField(max_length=5)
    progress_vote = models.IntegerField(default=0)