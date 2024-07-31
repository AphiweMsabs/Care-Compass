from flask import Blueprint, render_template, jsonify, request

locationPoints= Blueprint("map",__name__)

@locationPoints.route('/location',methods=['GET', 'POST'])

def map_page():

    return render_template("map.html")


@locationPoints.route('/map_location',methods=['GET', 'POST'])

def create_location():

    return render_template("map.html")
