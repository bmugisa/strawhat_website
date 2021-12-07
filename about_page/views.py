from django.shortcuts import render
import os
# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def about_page(request):
	return render(request, 'about.html', {})