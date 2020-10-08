from django.db import models
from django.utils.translation import ugettext_lazy as _


class Movie(models.Model):
    imdb_id =  models.CharField(max_length=255, unique=True, verbose_name=_('imdb_id'))
    title = models.CharField(max_length=1000, verbose_name=_('title'))
    year = models.IntegerField(verbose_name=_('year'))
    rated = models.CharField(max_length=1000, verbose_name=_('rated'))
    released = models.DateField(verbose_name=_('rated'))
    runtime = models.IntegerField(verbose_name=_('runtime'))
    gentre = models.CharField(max_length=1000, verbose_name=_('gentre'))
    director = models.CharField(max_length=1000, verbose_name=_('director'))
    writer = models.TextField(verbose_name=_('writer'))
    actors = models.TextField(verbose_name=_('actors'))
    plot = models.TextField(verbose_name=_('plot'))
    language = models.CharField(max_length=1000, verbose_name=_('language'))
    country = models.CharField(max_length=1000, verbose_name=_('country'))
    awards = models.CharField(max_length=1000, verbose_name=_('awards'))
