from flask import Blueprint, render_template, jsonify, request

registerUser= Blueprint("register",__name__)

@registerUser.route('/sign-up',methods=['GET', 'POST'])

def signUp():
     return render_template("index.html")