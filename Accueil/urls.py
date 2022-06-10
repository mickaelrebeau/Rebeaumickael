from django.urls import path

from .views import *

app_name = 'accueil'

urlpatterns = [
    path('', AccueilView.as_view(), name='accueil'),
    path('photos/', PhotosView.as_view(), name='photos'),
]
