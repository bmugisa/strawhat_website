from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('service/', views.service_page, name='service')
]