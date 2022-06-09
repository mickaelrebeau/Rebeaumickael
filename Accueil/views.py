from django.shortcuts import render
from django.views.generic import TemplateView


class AccueilView(TemplateView):
    template_name = 'accueil.html'
