#-*- coding:utf-8 -*-
from django.conf.urls import patterns, url
from monitoreo import views
from django.conf import settings

urlpatterns = patterns('',
                       url(r'^$', views.DispositivoIndex.as_view(), name="dispositivos"),
                       url(r'^(?P<slug>.+)$', views.DispositivoDetail.as_view(), name="dispositivo-detail"),                      
                      )