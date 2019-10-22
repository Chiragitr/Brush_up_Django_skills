import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# FBV views
def home(request):
	#return HttpResponse(html_)
	num = random.randint(0,10000)
	list = [123,random.randint(0,10000),random.randint(0,10000),random.randint(0,10000)]
	context_data = {
		"name":"Chirag Gupta",
		"Place":"Chennai",
		"num":num,"bool":True,
		"list":list
	}
	return render(request, "base.html",context_data)


def contact(request):
	#return HttpResponse(html_)
	num = random.randint(0,10000)
	list = [123,random.randint(0,10000),random.randint(0,10000),random.randint(0,10000)]
	context_data = {
		"name":"Chirag Gupta",
		"Place":"Chennai",
		"num":num,"bool":True,
		"list":list
	}
	return render(request, "contact.html",context_data)

def about(request):
	#return HttpResponse(html_)
	num = random.randint(0,10000)
	list = [123,random.randint(0,10000),random.randint(0,10000),random.randint(0,10000)]
	context_data = {
		"name":"Chirag Gupta",
		"Place":"Chennai",
		"num":num,"bool":True,
		"list":list
	}
	return render(request, "about.html",context_data)