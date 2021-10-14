from django.conf.urls import url

from admin.crime import views

urlpatterns = {
    url(r'^crime_model', views.create_crime_model),
    url(r'^police_position', views.create_police_position),
    url(r'^cctv_model', views.create_cctv_model),
    url(r'^population_model', views.create_population_model),
    url(r'^merge_cctv_pop', views.merge_cctv_pop),
    url(r'^process', views.process)
}




