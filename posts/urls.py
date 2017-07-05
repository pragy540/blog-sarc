from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^posts/([\w-]+)/$', views.post, name="post"),
]