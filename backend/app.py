#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
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
#    import os
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

# Predict
#   Make a prediction based on 
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()
            # @TODO: Validate Data
            
            query_data = data["vars"]
            
            model = joblib.load("./data/linear_regression_model.pkl")
        except ValueError as e:
            return jsonify("Error in prediction - {}".format(e))

        return jsonify(model.predict(query_data).tolist())


# add new data
# test that training & test error rates are similar
@app.route("/retrain", methods=['POST'])
def retrain():
    if request.method == 'POST':
        data = request.get_json()

        try:
            # Grab traing information stored on disk
            X_train = joblib.load("./data/training_X.pkl")
            y_train = joblib.load("./data/training_y.pkl")
            
            # Convert Array into DataFrame
            params_data = np.array(data['vars'])
            params_data = params_data.reshape(1, -1)
            xRow = pd.DataFrame(params_data, columns=X_train.columns.values)

            # Create DataFrame from Salary
            yRow = pd.DataFrame({'Salary': [data["Salary"]]})
            
            # Persisted Data with new data
            all_data = X_train.append(xRow)
            all_salaries = y_train.append(yRow)
            
            # new regression
            updated_model = LinearRegression()
            updated_model.fit(all_data, all_salaries)

            # remove old training data
            os.remove("./data/linear_regression_model.pkl")
            os.remove("./data/training_X.pkl")
            os.remove("./data/training_y.pkl")

            # generate new training data
            joblib.dump(updated_model, "./data/linear_regression_model.pkl")
            joblib.dump(all_data, "./data/training_X.pkl")
            joblib.dump(all_salaries, "./data/training_y.pkl")

            # sample prediction
            predict = updated_model.predict(data['vars'])

        except ValueError as e:
            return jsonify("Error when retraining - {}".format(e))

        return jsonify(predict.tolist())

app.run(host='0.0.0.0', port=8000, debug=True)    