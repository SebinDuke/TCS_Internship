from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/images/favicon.ico', permanent=True)

urlpatterns = [
    url(r'^', include('main.urls')),
    url(r'^user/', include('login.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^favicon\.ico$', favicon_view),
]
