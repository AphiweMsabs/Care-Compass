from flask import Flask
from flask import Flask, render_template, url_for, request, jsonify


def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']= "HELLO"

    return app