import datetime
from flask import Blueprint, render_template, jsonify, request
from .auth import firebase;

happenings= Blueprint("event",__name__)

items = [
    {
        'text': 'First Item',
        'image_url': 'https://via.placeholder.com/150',
        'timestamp': '2024-08-05 12:00:00'
    },
    {
        'text': 'Second Item',
        'image_url': 'https://via.placeholder.com/150',
        'timestamp': '2024-08-05 12:05:00'
    },
    {
        'text': 'Third Item',
        'image_url': 'https://via.placeholder.com/150',
        'timestamp': '2024-08-05 12:10:00'
    }
]

db=firebase.database()

@happenings.route('/events',methods=['GET', 'POST'])

def showcase_events():

   



    return render_template("showCaseEvents.html")

@happenings.route('/add-events',methods=['GET', 'POST'])

def event_creation():
    if request.method == "POST":
        event_name = request.form['event_name']
        host = request.form['host']
        date = request.form['date']
        description = request.form['description']
        
        # Create a new event
        new_event = {
            'event_name': event_name,
            'host': host,
            'date': date,
            'description': description,
            'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # current timestamp
        }

        # Push the new event to Firebase
        db.child("events").push(new_event)


    return render_template("showCaseEvents.html")