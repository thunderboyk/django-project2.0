from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# after generator, {'password':'aijemsuvw'} and call in the html file by using 2 {{password}} bracket 
def home(request):
	return render(request,'generator/home.html')


def password(request):
	return render(request,'generator/Password.html')
