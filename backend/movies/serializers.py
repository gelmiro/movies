from django.contrib.auth.models import User
from rest_framework import serializers

from movies.models import Movie


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = self.Meta.model.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie

        fields = ('id', 'users', 'imdbID', 'Title', 'Year', 'Type', 'Poster')


class OMDBSerializer(serializers.Serializer):
        imdbID = serializers.CharField()
        Title = serializers.CharField()
        Year = serializers.CharField()
        Type = serializers.CharField()
        Poster = serializers.CharField()