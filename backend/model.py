#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('./data/stackOverflowSalaryData2018.csv')

# All columns except 'Salary'
X = dataset.loc[:, dataset.columns != 'Salary']

# Salary column
y = dataset[['Salary']]


# Test/ Train split
#   If you wanted to do a Test/Train split
#   from sklearn.cross_validation import train_test_split
#   X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Building the optimal model using Backward elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones((3495,1)).astype(int), values = X, axis =1)

# Print a OLS report
#   Creates a report to examin variables
regressor_OLS = sm.OLS(endog = y, exog = X).fit()
regressor_OLS.summary()


# Avoiding the Dummy Variable Trap | remove 
# Dummy Variables: Company size, Type of dev, FormalEducation
# noUni[14], educLess[17], majorNA[22], compSize1[25]
# X = X[:, [0,1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,18,19,20,21,23,24,26,27,28,29,30,31,32,33,34]]
 X = X.drop(['noUni', 'educLess', 'majorNA', 'compSize1'], axis=1)


# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Pickle
joblib.dump(new_model, "./data/linear_regression_model.pkl")
joblib.dump(years_exp, "./data/training_X.pkl")
joblib.dump(salary, "./data/training_y.pkl")



