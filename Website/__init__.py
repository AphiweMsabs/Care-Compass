from flask import Flask
from flask import Flask, render_template, url_for, request, jsonify
import pyrebase


config={
    'apiKey': "AIzaSyC_4AVd9QKo74m77VUfVustsJQDo5joV3M",
  'authDomain': "care-compass-25253.firebaseapp.com",
  'databaseURL': "https://care-compass-25253-default-rtdb.firebaseio.com",
  'projectId': "care-compass-25253",
  'storageBucket': "care-compass-25253.appspot.com",
  'messagingSenderId': "306549999936",
  'appId': "1:306549999936:web:c9a25e370606972d2052a5",
  'measurementId': "G-2EXXRY9BER"
}

firebase= pyrebase.initialize_app(config)
auth=firebase.auth()




def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']= "HELLO"

    from .views import pages
    from .auth import registerUser
    from .home_page import home

    app.register_blueprint(pages, url_prefix='/')
    app.register_blueprint(registerUser, url_prefix='/')
    app.register_blueprint(home,url_prefix='/')

    return app