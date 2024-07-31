from flask import Blueprint, render_template, jsonify, request

happenings= Blueprint("event",__name__)

@happenings.route('/events',methods=['GET', 'POST'])

def showcase_events():
     return render_template("index.html")

@happenings.route('/create-events',methods=['GET', 'POST'])

def event_creation():
     return render_template("index.html")