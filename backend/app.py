#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
import logging
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib

try:
    from flask_cors import CORS  # The typical way to import flask-cors
except ImportError:
    # Path hack allows examples to be run without installation.
    import os
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)

    from flask_cors import CORS

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# To enable logging for flask-cors,
logging.getLogger('flask_cors').level = logging.DEBUG

# One of the simplest configurations. Exposes all resources matching /api/* to
# CORS and allows the Content-Type header, which is necessary to POST JSON
# cross origin.
CORS(app, resources=r'/*')


@app.route('/')
def home():
    return("How about some Machine Learning?")

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()
            years_of_experience = float(data["YearsExperience"])
            
            lin_reg = joblib.load("./data/linear_regression_model.pkl")
        except ValueError as e:
            return jsonify("Error in prediction - {}".format(e))

        return jsonify(lin_reg.predict(years_of_experience).tolist())

# @TODO: Alternative process for retraining
# add new data
# create new split?
# test that training & test error rates are similar
#   I.E. abort if everything is all fucked up
@app.route("/retrain", methods=['POST'])
def retrain():
    if request.method == 'POST':
        data = request.get_json()

        try:
            # grab traing information stored on disk
            X_train = joblib.load("./data/training_X.pkl")
            y_train = joblib.load("./data/training_y.pkl")
            X_test = joblib.load("./data/testing_X.pkl")

            # append the new data to the existing data set
            years_exp = np.append(X_train, data['YearsExperience'])
            salary = np.append(y_train, data["Salary"])

            # needs to be in the right format
            years_exp = years_exp.reshape(-1,1)

            # new regression
            new_model = LinearRegression()
            new_model.fit(years_exp, salary)


            # remove old training data
            os.remove("./data/linear_regression_model.pkl")
            os.remove("./data/training_X.pkl")
            os.remove("./data/training_y.pkl")

            # generate new training data
            joblib.dump(new_model, "./data/linear_regression_model.pkl")
            joblib.dump(years_exp, "./data/training_X.pkl")
            joblib.dump(salary, "./data/training_y.pkl")

            # sample prediction
            # pred = new_model.predict(X_test)
            # return jsonify(pred.tolist())

        except ValueError as e:
            return jsonify("Error when retraining - {}".format(e))

        return jsonify("Retrained model successfully.")

app.run(host='0.0.0.0', port=8000, debug=True)    