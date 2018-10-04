from django.urls import path, re_path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.view_core, name='overview'),
    path('character/create', views.create_character, name='createcharacter'),
    path('party/create', views.create_party, name='createparty'),
    path('scenario/create', views.create_scenario, name='createscenario'),
    re_path('party/(?P<party_id>[0-9]{1,})/', views.view_party, name='partydetail'),
    re_path('character/(?P<pk>[0-9]{1,})', views.UpdateCharacter.as_view(),
    name='character_update'),
]
