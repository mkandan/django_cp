from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

#a question has a question text and a publication date
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date>=timezone.now()-datetime.timedelta(days=1)

#a choice is it's own sheet. two parts question- referenced from
#what question you chose to answer earlier. and vote tally
class Choice (models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text