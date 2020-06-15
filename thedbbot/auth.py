import tweepy

consumer_token = ""
consumer_secret = ""
auth = tweepy.OAuthHandler(consumer_token,consumer_secret)

def authenticate_user():
	try:
		redirect_url = auth.get_authorization_url()
	except tweepy.TweepError:
		print('Error! Failed to get request token.')
	
	return redirect_url

def complete_auth(token, verifier):
	auth.request_token = { 'oauth_token' : token,'oauth_token_secret' : verifier }
	try:
		access_rights = auth.get_access_token(verifier)
	except tweepy.TweepError:
		print('Error! Failed to get access token.')
	
	return access_rights