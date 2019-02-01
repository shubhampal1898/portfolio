from django.shortcuts import render
from django.http import request
# Create your views here.
def home(request):
    render(request, 'jobs/home.html')
