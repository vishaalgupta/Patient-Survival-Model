<<<<<<< HEAD
from flask import Flask, render_template, redirect, jsonify, request
import json
import numpy as np
import pandas as pd
from joblib import dump, load



app = Flask(__name__)



##Need to add connection to model in line below
model = load('../ML-models/model_ExtraTrees.joblib')

@app.route("/")
def home():
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
        text = "Patient is not predicted to survive"
    else:
        text = "Patient is predicted to survive"

    # create html content - either single variable, dictionary, or string
    prediction_text = f"The survival prediction is: {text}."

    # send prediction to html page
    return render_template("index.html", result = prediction_text)



if __name__ == "__main__":
    app.run(debug=True)




=======
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
>>>>>>> 483ddaf1dd8f82da3bd438ff6b02a3098d917d83
