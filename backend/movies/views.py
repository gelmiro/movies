import requests
import pprint
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework import status

from movies.models import Movie
from .serializers import MovieSerializer, OMDBSerializer, UserSerializer


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

    def create(self, request, *args, **kwargs):
        request.data['users'] = [self.request.user.id]
        imdbID = request.data.get('imdbID')
        try:
            record = Movie.objects.get(imdbID=imdbID)
        except Movie.DoesNotExist:
            return super().create(request, *args, **kwargs)

        record.users.add(self.request.user)
        return Response({}, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.users.count() > 1:
            instance.users.remove(self.request.user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return super().destroy(request, *args, **kwargs)

    @action(detail=False)
    def omdb(self, request):
        params = {'apikey': settings.OMDB_APIKEY, **request.query_params}

        resp = requests.get(url=settings.OMDB_URL, params=params)
        payload = resp.json()
        pprint.pprint(payload)
        if resp.status_code != 200:
            raise ValidationError('Service is unavailable')
        elif 'True' != payload.get('Response', 'False'):
            raise ValidationError(payload.get('Error', 'Unknown Error'))

        serialized = self.omdb_response_validation(payload.get('Search', payload))
        response = {'data': serialized}
        self.add_meta(payload, response)

        return Response(response)

    def add_meta(self, payload, response):
        response['meta'] = {}
        total_results = payload.get('totalResults')
        if total_results:
            response['meta']['total_results'] = total_results

    def omdb_response_validation(self, data):
        if isinstance(data, dict):
            return self.record_validation(data)
        elif isinstance(data, list):
            return [self.record_validation(record) for record in data]
        else:
            raise ValidationError('OMDB schema Error')

    def record_validation(self, data):
        serialization = OMDBSerializer(data=data)
        serialization.is_valid(raise_exception=True)
        return serialization.validated_data
