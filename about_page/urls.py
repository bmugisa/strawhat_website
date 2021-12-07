from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('about/', views.about_page, name='about')
]