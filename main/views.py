from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django.urls import reverse
#for older versoins of Django use:
#from django.core.urlresolvers import reverse

import re

from login.models import User
from .models import Books
from .forms import AddBookForm

def index(request):
    li=Books.objects.order_by('-pk')[:10]
    if request.session.has_key('user_id'):
        uid=request.session['user_id']
        try:
            user=User.objects.get(user_name=uid)
            return render(request, 'Html/index.html',{'usr':user,'list':li})
        except User.DoesNotExist:
            return HttpResponse("UserName not found")
    else:
        return render(request, 'Html/index.html',{'list':li})

def donate(request,book):
    if request.session.has_key('user_id'):
        uid=request.session['user_id']
        try:
            user=User.objects.get(user_name=uid)
            bk=Books.objects.get(book_name=book)
            bk.no_of_copies+=1
            pts=bk.points
            bk.save()
            user.points+=pts
            user.save()
            li=Books.objects.order_by('-pk')[:10]
            return render(request, 'Html/donate.html',{'usr':user,'list':li,'book':book})
        except (User.DoesNotExist , Books.DoesNotExist):
            return HttpResponse('Book or user does not exist')
    else:
        return HttpResponseRedirect(reverse('login:login'))


def getbook(request,book):
    if request.session.has_key('user_id'):
        uid=request.session['user_id']
        try:
            user=User.objects.get(user_name=uid)
            bk=Books.objects.get(book_name=book)
            if bk.no_of_copies==0:
                return HttpResponse('The book'+book+'is out of stock')
            bk.no_of_copies-=1
            pts=bk.points
            bk.save()
            user.points-=pts
            user.save()
            li=Books.objects.order_by('-pk')[:10]
            return render(request, 'Html/getbook.html',{'usr':user,'list':li,'book':book})
        except (User.DoesNotExist , Books.DoesNotExist):
            return HttpResponse('Book or user does not exist')
    else:
        return HttpResponseRedirect(reverse('login:login'))


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
            p=Books(book_name=book.cleaned_data.get('bookname'),auth_name=book.cleaned_data.get('auth'),points=points,price=price,varification=False)
            p.save()
    
    return HttpResponseRedirect(reverse('main:index'))

def search(request):
    if request.method == 'POST':
        search=request.POST['search']
        #t=Topic.objects.get(topic_text=topic.cleaned_data.get('topic_text'))
        book_li = Books.objects.all()
        li=[]
        for b in book_li:
            if re.search(search,b.book_name,re.IGNORECASE):
                li.append(b)
            elif re.search(search,b.auth_name,re.IGNORECASE):
                li.append(b)
        if request.session.has_key('user_id'):
            uid = request.session['user_id']
            user = User.objects.get(user_name=uid)
            return render(request, 'Html/searchresults.html', {'user_id':user,"list": li})
        else:
            return render(request, 'Html/searchresults.html', {"list": li})
    else:
        return HttpResponse("not POST")