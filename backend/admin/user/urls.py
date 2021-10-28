from django.conf.urls import url

from admin.user import views

urlpatterns = {
    url(r'', views.users, name='users'),
    url(r'/login', views.login),
    url(r'/<slug:id>', views.users),   # delete
    url(r'', views.users, name='users'),
    url(r'', views.users, name='users'),

}