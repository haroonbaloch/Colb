
from django.conf.urls import url
from ColorBlind_App import views

urlpatterns = [
    url(r'^$',views.colors,name='colors'),
    url(r'^result', views.results, name='results'),
]
