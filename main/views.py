from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django.urls import reverse
#for older versoins of Django use:
#from django.core.urlresolvers import reverse

from login.models import User

def index(request):
    if request.session.has_key('user_id'):
        uid=request.session['user_id']
        try:
            user=User.objects.get(user_name=uid)
            return HttpResponse("Logged in as "+user.first_name)
        except User.DoesNotExist:
            return HttpResponse("UserName not found")
    else:
        return HttpResponse("You are not logged in")
