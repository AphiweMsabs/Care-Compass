from flask import Blueprint, render_template, jsonify, request

prof= Blueprint("profile",__name__)

@prof.route('/my_profile',methods=['GET', 'POST'])

def my_profile():
     return render_template("index.html")