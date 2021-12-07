from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('team/',views.team_page, name='team')
]