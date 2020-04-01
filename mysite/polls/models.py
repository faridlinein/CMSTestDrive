import datetime
from django.db import models

from django.utils import timezone


# ---Group Django models
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now= timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


"""NOTE_START 
from polls.models import Choice, Question

Question.objects.all()

Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith='What')

from django.utils import timezone
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)

Question.objects.get(id=2)

Question.objects.get(pk=1)

q = Question.objects.get(pk=1)s
q.was_published_recently()
q = Question.objects.get(pk=1)

q.choice_set.all()
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)

c.question
q.choice_set.all()
q.choice_set.count()
Choice.objects.filter(question__pub_date__year=current_year)

c = q.choice_set.filter(choice_text__startswith='Just hacking')
c.delete()
NOTE_END"""
