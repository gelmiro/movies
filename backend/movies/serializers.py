from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from movies.models import Movie


class UserSerializer(ModelSerializer):
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


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie

        fields = ('users', 'imdbID', 'Title', 'Year', 'Type', 'Poster')
