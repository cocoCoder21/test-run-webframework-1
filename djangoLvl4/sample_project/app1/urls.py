from django.conf.urls import url
from app1 import views

#TEMPLATE TAGGING
app_name = 'app1'

urlpatterns=[
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name = 'other'),
]
