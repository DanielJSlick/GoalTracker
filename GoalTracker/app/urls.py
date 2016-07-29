from django.conf.urls import include, url
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^app/', include('app.urls')),
    url(r'^admin/', admin.site.urls),
]