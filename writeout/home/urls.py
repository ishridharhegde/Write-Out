from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.homeRedirect),
    url('^home/$',  views.index),
    url('^contact/$',  views.contact),
]