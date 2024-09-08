from django.shortcuts import render
from django.http import HttpResponse
import random 
# Create your views here.
# after generator, {'password':'aijemsuvw'} and call in the html file by using 2 {{password}} bracket 
def home(request):
	return render(request,'generator/home.html')




def about(request):
	return render(request,'generator/about.html')







def password(request):
	
	charecters= list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('Uppercase'):

		charecters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWZYZ'))

	
	if request.GET.get('special'):

		charecters.extend(list('!@#$%^&*()_+'))

	if request.GET.get('numbers'):

		charecters.extend(list('1234567890'))	





	length = int(request.GET.get('length',14))


	# so 14 is the basic parameter or default length if noting is selescted 
# basically this code gets input from the user GET and translates it to the html input of length
	
	thepassword = ' '
	for x in range(length):
		thepassword+= random.choice(charecters)

	return render(request,'generator/Password.html',{'password':thepassword})

