from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class DashboardView(TemplateView):
    template_name = "dashboard.html"

# class WeatherView(TemplateView):
#     template_name="weather.html"