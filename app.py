from flask import Flask, render_template, redirect, jsonify
import json
import numpy as np
import pandas as pd
from bson import json_util

app = Flask(__name__)



##Need to add connection to model in line below
##model = load(open('./models/model_linregress_2022081800.pkl', 'rb'))

@app.route("/")
def home():
    prediction_text = ""
    eturn render_template("index.html", result = prediction_text)


@app.route("/send", methods=["POST"])
def send():
    icu_death_prob = request.form["icu"]
    ventilation = request.form["ventilation"]
    gcs_verbal = request.form["gscVerbal"]
    gcs_eye = request.form["gscEyes"]
    hos_death_prob = request.form['hospital']
    gcs_motor = request.form['gscMotor']
    min_sys_ni = request.form['bpNon']
    min_sis = request.form['bp']
    age = request.form['age']
    min_mean_bp = request.form['minBP']

    final_features = [np.array([icu_death_prob, ventilation, gcs_verbal, gcs_eye, hos_death_prob, gcs_motor, min_sys_ni, min_sis, age, min_mean_bp])]

    # use form results to make prediction
    prediction = model.predict(final_features)[0]

    # create html content - either single variable, dictionary, or string
    prediction_text = f"The survival prediction is: prediction."

    # send prediction to html page
    return render_template("index.html", result = prediction_text)



if __name__ == "__main__":
    app.run(debug=True)




