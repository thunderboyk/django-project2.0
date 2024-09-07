from django.shortcuts import render
from django.http import HttpResponse
import random 
# Create your views here.
# after generator, {'password':'aijemsuvw'} and call in the html file by using 2 {{password}} bracket 
def home(request):
	return render(request,'generator/home.html')

def password(request):
	
	charecters= list('abcdefghijklmnopqrstuvwxyz')

	length = 10

	thepassword = ' '
	for x in range(length):
		thepassword+= random.choice(charecters)

	return render(request,'generator/Password.html',{'password':thepassword})

