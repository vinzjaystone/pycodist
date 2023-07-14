from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect

def index(request):
    return HttpResponse("HELLO WORLD")