from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.view_core),
    path('party/', views.view_party),
]