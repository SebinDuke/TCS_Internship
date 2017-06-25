from django.conf.urls import url

from . import views

app_name = 'main' 

urlpatterns = [
    #url for home-page:
    url(r'^$', views.index, name='index'),

    #url for donate:
    url(r'donate$', views.donate, name='donate'),

    #url not used:
    url(r'donate-book$', views.donatebk,name='donate_book'),

    #url for addbook:
    url(r'addbook$', views.addbk,name='addbook'),

    #url for search:
    url(r'search$', views.search, name='search'),
]