from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.view_core, name='overview'),
    path('character/create', views.create_character, name='createcharacter'),
    path('party/create', views.create_party, name='createparty'),
]
