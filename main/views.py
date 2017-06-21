from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django.urls import reverse
#for older versoins of Django use:
#from django.core.urlresolvers import reverse

from login.models import User
from .models import Books
from .forms import AddBookForm

def index(request):
    if request.session.has_key('user_id'):
        uid=request.session['user_id']
        try:
            user=User.objects.get(user_name=uid)
            return render(request, 'Html/index.html',{'usr':user})
        except User.DoesNotExist:
            return HttpResponse("UserName not found")
    else:
        return render(request, 'Html/index.html')

def donate(request):
    if request.session.has_key('user_id'):
        uid=request.session['user_id']
        try:
            user=User.objects.get(user_name=uid)
            return render(request, 'Html/donate.html', {'usr':user})
        except User.DoesNotExist:
            return HttpResponse("UserName not found")
    else:
        return  HttpResponseRedirect(reverse('login:login'))

def donatebk(request):
    if request.session.has_key('user_id'):
        uid=request.session['user_id']
        try:
            user=User.objects.get(user_name=uid)
            if request.method == 'POST':
                bk_nm = request.POST['bookname'] 
                try:
                    book=Books.objects.get(book_name=bk_nm)
                    return render(request, 'Html/donate.html', {'usr':user,'book':book})
                except Books.DoesNotExist:
                    return render(request, 'Html/donate.html', {'usr':user,'book':"notyet"})
        except User.DoesNotExist:
            return HttpResponse('UserName not found')
    else:
        return HttpResponseRedirect(reverse('login:login'))


def addbk(request):
    if request.method == 'POST':
        book=AddBookForm(request.POST)
        if book.is_valid():
            price=int(book.cleaned_data.get('price'))
            points=int(price/10)
            p=Books(book_name=book.cleaned_data.get('bookname'),auth_name=book.cleaned_data.get('auth'),points=points,price=price)
            p.save()
    
    return HttpResponseRedirect(reverse('main:index'))

