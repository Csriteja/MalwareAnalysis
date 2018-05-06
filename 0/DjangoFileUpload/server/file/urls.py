from django.conf.urls import url
from . import views

app_name = 'file'

urlpatterns =[
    url(r'^$', views.index, name='index'),
]


