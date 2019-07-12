from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings
from django.urls import include, path,re_path

app_name = 'myechartsite'
urlpatterns = [
    url(r'^firstindex$', views.firstindex, name='firstindex'),
    url(r'^index_customer/$', views.index_customer, name='index_customer'),
    url(r'^index_expert/$', views.index_expert, name='index_expert'),
    url(r'^index_doctor/$', views.index_doctor, name='index_doctor'),
    url(r'^login/', views.login, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^changeinfo/', views.changeinfo, name='changeinfo'),

    path('index_customer/', include([
        path('inditrend', views.inditrend,name='inditrend'),
        path('inditrend_data', views.inditrend_data,name='inditrend_data'),
        path('userindi', views.userindi,name='userindi'),
        path('userindi_data', views.userindi_data,name='userindi_data'),
        re_path('articles/(\d+)', views.article, name='article'),
        path('search/', views.search, name='search'),
        path('changece/', views.changece, name='changece'),
        path('hospitalmap', views.hospitalmap, name='hospitalmap'),
        path('hospitalmap_data', views.hospitalmap_data, name='hospitalmap_data'),
        path('article_collected/', views.article_collected, name='article_collected'),
        ])),
    path('index_expert/', include([
        path('disewheather', views.disewheather,name='disewheather'),
        path('disewheather_data', views.disewheather_data,name='disewheather_data'),
        path('diseage', views.diseage, name='diseage'),
        path('diseage_data', views.diseage_data, name='diseage_data'),
        path('disegender', views.disegender, name='disegender'),
        path('disegenderage_data', views.disegenderage_data, name='disegenderage_data'),
        path('disetemp', views.disetemp, name='disetemp'),
        path('disetemp_data', views.disetemp_data, name='disetemp_data'),
        path('diseyear', views.diseyear, name='diseyear'),
        path('diseyear_data', views.diseyear_data, name='diseyear_data'),
        path('diseaqi', views.diseaqi, name='diseaqi'),
        path('diseaqi_data', views.diseaqi_data, name='diseaqi_data'),
        path('disemonth', views.disemonth, name='disemonth'),
        path('disemonth_data', views.disemonth_data, name='disemonth_data'),
        path('arearatiomap', views.arearatiomap, name='arearatiomap'),
        path('arearatiomap_data', views.arearatiomap_data, name='arearatiomap_data'),
        path('arearatiochange', views.arearatiochange, name='arearatiochange')
        ])),

    path('index_doctor/', include([
        path('diseindicator', views.diseindicator, name='diseindicator'),
        path('diseindicator_data', views.diseindicator_data, name='diseindicator_data')
        ])),


    # url(r'^index_customer/articles/(\d+)$', views.article, name='article'),
    # url(r'^index_customer/search/', views.search, name='search'),
    # url(r'^index_expert/disewheather$', views.disewheather, name='disewheather'),
    # url(r'^index_expert/disewheather_data$', views.disewheather_data, name='disewheather_data'),
    # url(r'^index_expert/diseage$', views.diseage, name='diseage'),
    # url(r'^index_expert/diseage_data$', views.diseage_data, name='diseage_data'),
    # url(r'^index_expert/disegender$', views.disegender, name='disegender'),
    # url(r'^index_expert/disegenderage_data$', views.disegenderage_data, name='disegenderage_data'),
    # url(r'^index_customer/userindi', views.userindi, name='userindi'),
    # url(r'^index_customer/userindi_data', views.userindi_data, name='userindi_data'),
    # url(r'^index_doctor/diseindicator$', views.diseindicator, name='diseindicator'),
    # url(r'^index_doctor/diseindicator_data$', views.diseindicator_data, name='diseindicator_data'),
    # url(r'^index_expert/disetemp$', views.disetemp, name='disetemp'),
    # url(r'^index_expert/disetemp_data$', views.disetemp_data, name='disetemp_data'),
    # url(r'^index_customer/inditrend$', views.inditrend, name='inditrend'),
    # url(r'^index_customer/inditrend_data$', views.inditrend_data, name='inditrend_data'),
    # url(r'^index_expert/diseyear$', views.diseyear, name='diseyear'),
    # url(r'^index_expert/diseyear_data$', views.diseyear_data, name='diseyear_data'),
    # url(r'^index_expert/disemonth$', views.disemonth, name='disemonth'),
    # url(r'^index_expert/disemonth_data$', views.disemonth_data, name='disemonth_data'),
    # url(r'^index_expert/diseaqi$', views.diseaqi, name='diseaqi'),
    # url(r'^index_expert/diseaqi_data$', views.diseaqi_data, name='diseaqi_data'),
    # url(r'^index_expert/arearatiomap$', views.arearatiomap, name='arearatiomap'),
    # url(r'^index_expert/arearatiomap_data$', views.arearatiomap_data, name='arearatiomap_data'),
    # url(r'^index_expert/arearatiochange$', views.arearatiochange, name='arearatiochange'),
    # url(r'^index_customer/article_collected/', views.article_collected, name='article_collected'),
    # url(r'^index_customer/changece/', views.changece, name='changece'),
    # url(r'^index_customer/hospitalmap$', views.hospitalmap, name='hospitalmap'),
    # url(r'^index_customer/hospitalmap_data$', views.hospitalmap_data, name='hospitalmap_data'),
]
