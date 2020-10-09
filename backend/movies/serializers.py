from django.contrib.auth.models import User
from rest_framework.fields import DateField

from movies.models import Movie
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email')


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie

        fields = ( 'users', 'imdbID', 'Title', 'Year', 'Type', 'Poster')
