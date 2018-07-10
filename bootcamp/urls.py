from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
	path('', views.indexPage , name='index'),
	path('signUp', views.signUp, name='signUp'),
	path('myPage', views.profile, name='profile'),
	path('articles', views.articles , name='articles'),
	path('messages', views.messages , name='messages'),
	path('articles/create', views.create_articles, name='create_articles')
	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)