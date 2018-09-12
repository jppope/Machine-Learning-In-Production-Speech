#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# NOTE: This code could do either a simple or multi linear regression
#
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Utilities
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib


# Importing the dataset
dataset = pd.read_csv('./data/stackOverflowSalaryData.csv')

# Salary column
y = dataset[['Salary']]

# All columns except 'Salary'
X = dataset.loc[:, dataset.columns != 'Salary']


# Variable Cleanup
#   We decided to purposely exclude certian variables
#   after evaluating the changes it made ~0.3% and it
#   helped make it easier for us

# Remove certain jobs
arr = ['graphic', 'embServ', 'QA', 'sysAdmin'] 

# Remove School nuances
arr += ['partUni', 'fullUni', 'educSome', 'majorSTEM', 'majorNonSTEM']

# Remove spaces
arr += ['spaces']

# Drop Variables
X = X.drop(arr, axis=1)


# Test/ Train split 
# ... In Case you want to do Simple Linear with this code.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Building the optimal model using Backward elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((3495,1)).astype(int), values = X, axis =1)

# Print a OLS report
#   Creates a report to examin variables
regressor_OLS = sm.OLS(endog = y, exog = X).fit()
regressor_OLS.summary()


# Salary
# ProgramHobby, YearsProgram, YearsCodedJob, 
# webdev, mobiledev, ML, devOps, desktop, database, other,
# educBA, educMA, educPhD, tabs, 
# smallComp, medComp, largeComp


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

# prediction
salary_prediction = model.predict(X_test)


# Pickle
joblib.dump(model, "./data/linear_regression_model.pkl")
joblib.dump(X_train, "./data/training_X.pkl")
joblib.dump(y_train, "./data/training_y.pkl")
joblib.dump(X_test, "./data/testing_X.pkl")
joblib.dump(y_test, "./data/testing_y.pkl")


