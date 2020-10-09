import requests
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from movies.models import Movie
from .serializers import MovieSerializer, UserSerializer


class CreateUserViewset(viewsets.ViewSetMixin, CreateAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_queryset(self):
        return self.queryset.filter(users=self.request.user)

    @action(detail=False)
    def omdb(self, request):
        params = {'apikey': settings.OMDB_APIKEY, **request.query_params}

        resp = requests.get(url=settings.OMDB_URL, params=params,
                            proxies={'http': 'http://87.254.212.120:8080'})
        payload = resp.json()
        if resp.status_code != 200:
            raise ValidationError('Service is unavailable')
        elif 'True' != payload.get('Response', 'False'):
            raise ValidationError(payload.get('Error', 'Unknown Error'))

        serialized = self.omdb_response_validation(payload.get('Search', payload))

        return Response(serialized)

    def omdb_response_validation(self, data):
        if isinstance(data, dict):
            return self.record_validation(data)
        elif isinstance(data, list):
            return [self.record_validation(record) for record in data]
        else:
            raise ValidationError('OMDB schema Error')

    def record_validation(self, data):
        serialization = MovieSerializer(data=data)
        serialization.is_valid(raise_exception=True)
        return serialization.validated_data
