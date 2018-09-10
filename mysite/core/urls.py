from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_core, name='core'),
    path('party/', views.view_party, name='party'),
]