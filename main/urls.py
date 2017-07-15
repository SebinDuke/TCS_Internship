from django.conf.urls import url

from . import views

app_name = 'main' 

urlpatterns = [
    #url for home-page:
    url(r'^$', views.index, name='index'),

    #url for donate:
    url(r'^(?P<book>[\w,\s]+)/donate/$', views.donate, name='donate'),

    #url for donate:
    url(r'^(?P<book>[\w,\s]+)/getbook/$', views.getbook, name='getbook'),

    #url not used:
    url(r'^donate-book/$', views.donatebk,name='donate_book'),

    #url for addbook:
    url(r'^addbook$', views.addbk,name='addbook'),

    #url for search:
    url(r'^search$', views.search, name='search'),

    #url for search:
    url(r'^confirm$', views.confirm, name='confirm'),

    #url for search:
    url(r'^orders$', views.orders, name='orders'),

]