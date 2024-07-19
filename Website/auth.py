from flask import Blueprint, redirect, render_template, jsonify, request,flash,session, url_for
from flask_mail import Mail, Message
# from email_validator import validate_email, EmailNotValidError
from functools import wraps
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

registerUser= Blueprint("register",__name__)

@registerUser.route('/sign-up',methods=['GET', 'POST'])
def signUp():
    if request.method == "POST":

      name = request.form.get("firstName")
      email=request.form.get("email")
      surname=request.form.get("lastName")
      password=request.form.get("password")
      password2=request.form.get("password2")

      if password != password2:
         flash("Passwords do not match", category='error')

      else:
           try:
                user=auth.create_user_with_email_and_password(email,password)
                flash("Successfully created an account with us", category='success')

                print(user)

           except:
                return 'Failed to sign up'
        

    return render_template("signUp.html")


@registerUser.route('/login',methods=['GET', 'POST'])

def login():
      
     
      if request.method == "POST":

        name = request.form.get("firstName")
        email=request.form.get("email")
        password=request.form.get("password")

        try:
            user=auth.sign_in_with_email_and_password(email,password)
            print(user)
            session['user']=email
            flash("Well Done", category='success')
        except:
                return 'Failed to login'
        
      return render_template("login.html")

def is_logged_in(f):
   @wraps(f)
   def wrap(*args, **kwargs):
         if 'logged_in' in session:
            return f(*args, **kwargs)
         else:
            flash('Unauthorized Access, Please login', category='error')
            return redirect(url_for('pages.login'))

   return wrap     


   


def logout():
    session.pop()
    return render_template("home.html")


