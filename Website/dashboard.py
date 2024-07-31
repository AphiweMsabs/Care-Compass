from flask import Blueprint, render_template

dash= Blueprint("dashboard",__name__)

@dash.route('/my-dashboard',methods=['GET', 'POST'])

def dashboard_page():
     return render_template("index.html")