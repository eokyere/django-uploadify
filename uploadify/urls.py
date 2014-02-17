from django.conf.urls import *

import views

urlpatterns = patterns('',
    url(r'^uploaded_view/$', views.uploaded_view),
    url(r'^upload/', views.upload),
)

