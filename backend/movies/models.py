from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Movie(models.Model):
    users = models.ManyToManyField(User, related_name='movies')
    imdbID =  models.CharField(max_length=255, unique=True, verbose_name=_('imdb_id'))
    Title = models.CharField(max_length=1000, verbose_name=_('title'))
    Year = models.CharField(max_length=255, verbose_name=_('year'))
    Type = models.CharField(max_length=255, verbose_name=_('type'))
    Poster = models.CharField(max_length=1000, verbose_name=_('poster'))
