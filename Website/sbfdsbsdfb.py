# from Website import create_app
from flask import Blueprint, render_template, jsonify, request, Flask
# app=create_app()
app = Flask(__name__)


@app.route('/')

def index():
    return render_template("index.html")

# @app.route('/', methods=['GET', 'POST'])


# def index():
#      name = request.form.get("first-name")
#      print(name)
#      print(jsonify({"key" : name}))
   
#      return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)