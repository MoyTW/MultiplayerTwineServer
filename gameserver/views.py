from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import GameSession

def index(request):
  return HttpResponse("TODO: Put some text here telling people they shouldn't be here.")

def session_state(request, session_id, client_id):
  session: GameSession = get_object_or_404(GameSession, pk=session_id)
  return HttpResponse(str(session.game_state))
