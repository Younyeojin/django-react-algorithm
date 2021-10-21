from django.conf.urls import url
from admin.iris import views

urlpatterns = {
    url(r'base', views.base)}