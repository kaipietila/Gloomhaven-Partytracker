from django.urls import path

from . import views

urlpatterns = [
    path('core/', views.view_core, name='core'),
]