from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# FBV views
def home(request):
	html_= """
		<h1>Heloo</h1>
		<p>This is nice!! we can place html inside views,\n is it good Practice?</p>
	"""
	return HttpResponse(html_)