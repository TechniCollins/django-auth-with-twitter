# Twitter-OAuth-with-Django-Tweepy

The primary role of the app is to provide authentication through Twitter for your users.

Ultimately, the item returned is the auth object, which you can store in your database. This django app focuses
only on the collection of the auth credentials, what you do with the access is entirely your choice 

CONFIGS

Twitter app

You have to create an app through your Twitter developer account first. Since we are using a web app,
you will need to set your 'callback url'. This is where Twitter will redirect your users after they 
succesfully authenticate. for this app, we are using 'http://127.0.0.1:8000/complete_ver' as our callback
url. You can change this to something else

Create a django app within your project. For this, the app is called 'thedbbot'. Create a file called auth.py in your
app directory.

Settings.py

    [os.path.join(BASE_DIR, "templates")]

project urls.py

    urlpatterns = [
	path('', include('thedbbot.urls')),
	path('signup/', include('thedbbot.urls')),
    path('admin/', admin.site.urls),
    path('complete_ver/', include('thedbbot.urls')),
    ]

app urls.py

    urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name ='signup'),
    path('complete_ver/', views.complete_ver, name = 'complete_ver')
    ]

Here are the functions of the different files in the app;

 1: templates/index.html - Replace this with your registration page. This just provides a place for the users to click in order
 to be redirected to the 'signup' page. I know the naming's a little confusing, sorry :(

 2: thedbbot/auth.py - This is where ALL the magic happens.
   Let's break down what the different functions do;
     
     authenticate_user()
   This returns an authorization url which our user will use to sign in to Twitter to authorize our app.
     
     complete_auth()
   This takes two arguments, verifier and OAuth_token, which are returned by Twitter after our user grants access to our app.
   Then it generates access token and access token secret keys.

 3: views.py
   The signup view calls the authenticate_user()
   The complete_ver view calls the complete_auth() function
