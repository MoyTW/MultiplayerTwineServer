from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

def index(request):
  return HttpResponse("TODO: Put some text here telling people they shouldn't be here.")
