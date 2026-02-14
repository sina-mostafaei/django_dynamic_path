from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.wel),
    path('product/<id>', views.reporter),
    path('product/<text>', views.t_rep),
]
