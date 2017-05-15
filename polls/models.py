import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    def __str__(self):
        return self.question_text

    def published_recently(self):
        return self.pub_date >= timezone.now()

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

datetime.timedelta(days=1)

class Choice(models.Model):
    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)