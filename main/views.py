from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django.urls import reverse
#for older versoins of Django use:
#from django.core.urlresolvers import reverse


def index(request):
    return HttpResponse("Index page")
