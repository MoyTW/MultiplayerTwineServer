from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('session/<uuid:session_id>/<uuid:client_id>', views.session_state, name='session_state'),
]