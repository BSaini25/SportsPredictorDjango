from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # url(r'^result/$', views.result, name='result'),
]