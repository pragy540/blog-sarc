from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^posts/(\w+)/$', views.post, name="post"),
    url(r'^history-of-the-campus/', views.hotc, name="hotc"),
    url(r'^alumni-and-research/', views.alumni_research, name="alumni_research"),
    url(r'^tete-a-tete-with-prof/', views.prof_interview, name="prof_interview"),
    url(r'^know-your-alumni/', views.kya, name="kya")
]