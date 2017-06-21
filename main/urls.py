from django.conf.urls import url

from . import views

app_name = 'main' 

urlpatterns = [
    #url for home-page:
    url(r'^$', views.index, name='index'),

    #url for donate-page:
    url(r'donate$', views.donate, name='donate'),

    #url for donate-book:
    url(r'donate-book$', views.donatebk,name='donate_book'),

    #url for donate-book:
    url(r'addbook$', views.addbk,name='addbook'),
]