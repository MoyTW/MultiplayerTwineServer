from django.urls import path

from gameserver import views

urlpatterns = [
  path('', views.index, name='index'),
]