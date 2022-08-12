from flask import Flask, render_template, redirect, jsonify
import json
import numpy as np
import pandas as pd
from bson import json_util

app = Flask(__name__)

@app.route("/")
def index():
    prediction_text = ""
    return render_template("index.html", result = prediction_text)

@app.route("/result")
def barchart():

    #prediction = model 

    #prediction_text = f"Based on the inputs, the model predicts the patient will {prediction}"
    return render_template("index.html", result = prediction_text)

# How to open a new page
""" @app.route("/map")
def map():
    return render_template("index-map.html") """


@app.route("/home")
def homepage():
    return(
        f"Patient Survival Model <br/>"
        f"Available Routes:<br/>"
        #f"/api/v1.0/dashboard<br>"
    )

if __name__ == "__main__":
    app.run(debug=True)
