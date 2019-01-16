from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings

app_name = 'myechartsite'
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^radar/',views.radar, name='radar'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register,name='register'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^disewheather/', views.disewheather, name='disewheather'),
]
