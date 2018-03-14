#-*- coding:utf-8 -*-
from django.conf.urls import patterns, url
from monitoreo import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = patterns('',
                       url(r'^$', views.DispositivoIndex.as_view(), name="dispositivos"),
                       url(r'^(?P<slug>.+)$', views.DispositivoDetail.as_view(), name="dispositivo-detail"),                      
                      )

urlpatterns += staticfiles_urlpatterns()
