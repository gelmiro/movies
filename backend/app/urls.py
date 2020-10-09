"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from movies import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'movies', views.MovieViewSet)

api_urls = [
    url(r'^v1/', include([
        # JSON API resources
        url(r'^', include(router.urls)),

        # JSON Web Token
        url(r'^api_token_obtain/$', obtain_jwt_token, name='api_token_obtain'),
    ]))
]

urlpatterns = [
    url('^admin/', admin.site.urls),
    url('^auth/', include('rest_framework.urls')),
    url(r'^api/', include(api_urls)),
]
