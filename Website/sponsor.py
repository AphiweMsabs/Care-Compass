from flask import Blueprint, render_template, jsonify, request

sponsor_facility= Blueprint("sponsorship",__name__)

@sponsor_facility.route('/sponsor',methods=['GET', 'POST'])

def sponsor_page():
     return render_template("sponsor.html")