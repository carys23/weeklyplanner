from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from datetime import datetime, timedelta
from calendar import HTMLCalendar
import datetime
from django.urls import reverse



class Week(models.Model):

    class Day(models.IntegerChoices):
        Monday = 0
        Tuesday = 1
        Wednesday = 2
        Thursday = 3
        Friday = 4
        Saturday = 5
        Sunday = 6

    days = models.IntegerField(choices=Day.choices)



class Note(models.Model):
    notes = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    day = models.DateTimeField(default=datetime.date.today)

def __str__(self):
    return (f"{self.notes}")  

# @property
# def get_html_url(self):
#     url = reverse('event_edit', args=(self.id,))
#     return f'<p>{self.notes}</p><a href="{url}">edit</a>'

