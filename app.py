from flask import Flask, render_template, redirect, jsonify, request
import json
import numpy as np
import pandas as pd
from joblib import dump, load



app = Flask(__name__)



##Need to add connection to model in line below
model = load('ML-models/model_ExtraTrees.joblib')

@app.route("/")
def homepage():
    return render_template("home.html")

@app.route("/visualizations")
def visualizations():
    return render_template("visualizations.html")

@app.route("/linearregression")
def linearregression():
    return render_template("linearregression.html")

@app.route("/logisticregression")
def logisticregression():
    return render_template("logisticregression.html")

@app.route("/knn")
def knn():
    return render_template("knn.html")

@app.route("/randomforest")
def randomforest():
    return render_template("randomforest.html")

@app.route("/adaboost")
def adaboost():
    return render_template("adaboost.html")

@app.route("/extratrees")
def extratrees():
    return render_template("extratrees.html")

@app.route("/About")
def about():
    return render_template("About.html")

@app.route("/Contact")
def contact():
    return render_template("Contact.html")

@app.route("/index")
def index():
    prediction_text = ""
    return render_template("index.html", result = prediction_text)


@app.route("/send", methods=["POST"])
def send():
    icu_death_prob = float(request.form["icu"])
    ventilation = float(request.form["ventilation"])
    gcs_verbal = float(request.form["gscVerbal"])
    gcs_eye = float(request.form["gscEyes"])
    hos_death_prob = float(request.form['hospital'])
    gcs_motor = float(request.form['gscMotor'])
    min_sys_ni = float(request.form['bpNon'])
    min_sis = float(request.form['bp'])
    age = float(request.form['age'])
    min_mean_bp = float(request.form['minBP'])

    final_features = [np.array([icu_death_prob, ventilation, gcs_verbal, gcs_eye, hos_death_prob, gcs_motor, min_sys_ni, min_sis, age, min_mean_bp])]

    # use form results to make prediction
    prediction = model.predict(final_features)[0]

    text =""

    if prediction == 1:
        text = "Patient is predicted to not survive"
    else:
        text = "Patient is predicted to survive"

    # create html content - either single variable, dictionary, or string
    prediction_text = "The survival prediction is: {}".format(text) 

    # send prediction to html page
    return render_template("index.html", result = prediction_text)



if __name__ == "__main__":
    app.run(debug=True)




