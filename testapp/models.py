import datetime
from django.utils import timezone
from django.db import models

class Yakiniku(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    #def __unicode__(self):
    def __str__(self):
        return self.name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <  now

class Choice(models.Model):
    yakiniku = models.ForeignKey(Yakiniku)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    #def __unicode__(self):
    def __str__(self):
        return self.choice_text