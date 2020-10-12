from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

from movies.models import Movie


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='user', password='password')
        User.objects.create(username='user2', password='password', first_name='first_name', last_name='last_name')

    def test_user_has_only_username(self):
        user = User.objects.get(username='user')
        self.assertEqual(user.username, 'user')

    def test_user_has_username_first_and_last_name(self):
        user = User.objects.get(username='user2')
        self.assertEqual(user.first_name, 'first_name')
        self.assertEqual(user.last_name, 'last_name')


class MovieTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user', password='password')
        movie = Movie.objects.create(imdbID='id1', Title='title1', Year='1', Type='type1', Poster='poster1')
        movie.users.add(self.user)

    def test_user_has_one_movie(self):
        self.assertEqual(self.user.movies.count(), 1)


class AuthorizationTestCase(TestCase):
    def setUp(self):
        self.base_url = '/api/v1'
        self.user = User.objects.create(username='user')
        self.user.set_password('password')
        self.user.save()

    def test_unathorized_request_to_api_root_is_rejected(self):
        client = APIClient()
        response = client.get(f'{self.base_url}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_unathorized_request_to_movies_is_rejected(self):
        client = APIClient()
        response = client.get(f'{self.base_url}/movies/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_registration_is_not_restricted_and_create_new_user(self):
        client = APIClient()
        response = client.post(f'{self.base_url}/register/', {
            'username': 'user_new',
            'password': 'password_new'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        User.objects.get(username='user_new')

    def test_login_view_returns_token_for_correct_credentials(self):
        client = APIClient()
        response = client.post(f'{self.base_url}/api_token_obtain/', {
            'username': 'user',
            'password': 'password'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        serializer = VerifyJSONWebTokenSerializer(data=response.data)
        serializer.is_valid(raise_exception=True)
        self.assertEqual(self.user, serializer.validated_data['user'])
