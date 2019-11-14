from django.urls.conf import include
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'CANDY'

# urlpatterns a lista de roteamentos de URLs para funções/Views
urlpatterns = [
    # GET /
    path('', views.voto_off, name='voto_off'),
    path('votee/<str:date>', views.voto_on, name='voto_on'),

]