from django.conf.urls import url
from django.contrib.auth.views import login, logout

from . import views


urlpatterns = [
    url(r'', views.MainPage.as_view(), name="mainPage"),
]