from django.shortcuts import render
from django.http import HttpResponse
from .auth import *
from django.shortcuts import redirect

#This is the view responsible for the entire signup
#This one is just a dummy, replace it with a better one
def index(request):
	return render(request, 'index.html')

def signup(request):
	result = redirect(authenticate_user())
	return result

#This view calls the complete(auth) function from auth.py
#which exchanges request token for the auth_token and auth_token secret
def complete_ver(request):
	auth_token = request.GET['oauth_token']
	verifier = request.GET['oauth_verifier']
	oauths = complete_auth(auth_token, verifier)
	#Store the following keys instead of displaying them as raw html
	return HttpResponse('<h1>' + verifier + '</h1' + '<br>' + '<h1>' + auth_token + '</h1>' + str(oauths))