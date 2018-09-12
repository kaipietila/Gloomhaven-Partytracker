from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.view_core),
    path('party/', views.view_party),
    path('character/create', views.create_character),
    path('party/create', views.create_party),
]