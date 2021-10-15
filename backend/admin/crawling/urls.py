from django.conf.urls import url
from admin.crawling import views

urlpatterns = {
    url(r'process', views.process),
    url(r'samsung_report', views.samsung_report),
    url(r'naver_movie', views.naver_movie),
    url(r'tweet_trup', views.tweet_trup),
}