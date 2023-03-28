# -*- coding: utf-8 -*-
"""Medical Insurance Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G1wAUnbQVU7yVlg8bTtuJlnWD-98fI7R

# Health Insurance Cost Prediction

### This project is carried out to predict the cost of the health insurance of the person based on the past data available such as age, gender, BMI, smoking habits, family detais etc.


### The same data is used to predict and propose the insurance price for the person based on details provided.
"""

# Importing the python libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

# Creating a raw dataset.
df_raw = pd.read_excel('/content/Health_insurance_cost.xlsx')

# Taking a copy of raw dataset.
df = df_raw.copy()

# To check the first 5 entries in the dataset.
df.head()

# To check the last 5 entries in the dataset.
df.tail()

df.shape # to check the shape of data set i.e. rows and columns.

# Print the number of columns and rows.
print("No of rows: ", df.shape[0])
print("No of columns: ", df.shape[1])

df.dtypes # To check the datatype of each columns

df.columns # To check the column data

df.info() # To check the information of the dataset

# Let's check for the unique values in our data

df.nunique()

# To check the null entries in the dataset.
df.isnull().sum()

# To check the null entries in the dataset.
df.isna().sum()

"""There are missong values in the data set.

28 in age, 23 in BMI and 2 in insurance price. 
"""

# To check the % of null entries in the dataset.
percent_missing = df.isnull().sum()*100/len(df)
percent_missing

"""### We will replace the missing values with median, mode since the missing value count is less that 2% in the entire data set."""

# msno.bar is a simple visualization of null values by column:

msno.bar(df.sample(1338))

sorted = df.sort_values('gender')
msno.matrix(sorted)

"""### Handling missing values in numerical columns using the median values."""

# Median values for columns age, BMI, health_insurance_price.
median1 = df["age"].median()
median2 = df["BMI"].median()
median3 = df["health_insurance_price"].median()
print(median1)
print(median2)
print(median3)

df.head() # Checking the data set for updates

df[['age','BMI','health_insurance_price']].dtypes # Checking the data set for updates

# Replacing the missng values using median values.
# for putting the value we use inplace

df["age"].replace(np.NaN,median1,inplace=True)
df["BMI"].replace(np.NaN,median2,inplace=True)
df["health_insurance_price"].replace(np.NaN,median3,inplace=True)

df.isnull().sum() # Checking the data set for updates.

df.info() # Checking the data set for updates

df.describe() # Checking the data set for updates

df.describe(include = 'all') # Checking the data set for updates

# Let's check for the unique values in our data

df.nunique()

df['location'].value_counts()

df.head(10)

# Checking the duplicate values.
duplicate = df.duplicated()
print(duplicate.sum())

df['gender'].unique() # Checking the unique data in dataset

# Converting the categorical data to numerical data using map / replace function.
df['gender'] = df['gender'].replace({'female' : 0, 'male' : 1})

df.head()

# Converting the categorical data to numerical data using map / replace function.
df['smoking_status'] = df['smoking_status'].replace({'no' : 0, 'yes' : 1})

df.head()

# Converting the categorical data to numerical data using map / replace function.
df['location'] = df['location'].map({'southwest' : 1, 'southeast' : 2,'northwest':3,'northeast': 4})

df.head()

"""### Model Building for Machine Learning Algorithms."""

# Checking the DV and IDV columns
df.columns

X = df.drop("health_insurance_price", axis = 1)

Y = df["health_insurance_price"]

print(X.head())

print(Y.head())

"""### Train / Test Split of Data:
1. Split the data into training and test data
2. Train the model on training data
3. Test the model on test data.
"""

# import sklearn library
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2, random_state = 42)

X_train

X_test

Y_train

Y_test

"""### Importing the Regression Models from sklearn library"""

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import metrics

"""# Model Training:

# 1. Linear Regression
"""

LR = LinearRegression()
LR.fit(X_train,Y_train)

LR.fit(X_train,Y_train)

# prediction on Training data
LR_tn_pred = LR.predict(X_train)

# R squared Error: Goodness of fit
LR_score_train = metrics.r2_score(Y_train, LR_tn_pred)
print("R squared Error : ", LR_score_train)

# prediction on Training data
LR_ts_pred = LR.predict(X_test)

# R squared Error: Goodness of fit
LR_score_test = metrics.r2_score(Y_test, LR_ts_pred)
print("R squared Error : ", LR_score_test)

"""# 2. Lasso Regression"""

# loading the lasso regression model
LS = Lasso()

LS.fit(X_train,Y_train)

# prediction on Training data
LS_tn_pred = LS.predict(X_train)

# R squared Error: Goodness of fit
LS_score_train = metrics.r2_score(Y_train, LS_tn_pred)
print("R squared Error : ", LS_score_train)

# prediction on Test data
LR_ts_pred = LS.predict(X_test)

# R squared Error: Goodness of fit
LS_score_test = metrics.r2_score(Y_test, LR_ts_pred)
print("R squared Error : ", LS_score_test)

"""# 3. Decision Tree Regressor"""

# loading the SVR model
DTR = DecisionTreeRegressor(criterion = "squared_error", max_depth=2, min_samples_split=10 )

DTR.fit(X_train,Y_train)

# prediction on Training data
DTR_tn_predict = DTR.predict(X_train)

# R squared Error: Goodness of fit
DTR_score_train = metrics.r2_score(Y_train, DTR_tn_predict)
print("R squared Error : ", DTR_score_train)

# prediction on Test data
DTR_ts_predict = LS.predict(X_test)

# R squared Error: Goodness of fit
DTR_score_test = metrics.r2_score(Y_test, DTR_ts_predict)
print("R squared Error : ", DTR_score_test)

"""# 4. Random Forest Regressor"""

# loading the Random Forest Regressor model
RFR = RandomForestRegressor(n_estimators=50, max_depth=4)

RFR.fit(X_train,Y_train)

# prediction on Training data
RFR_tn_predict = RFR.predict(X_train)

# R squared Error: Goodness of fit
RFR_score_train = metrics.r2_score(Y_train, RFR_tn_predict)
print("R squared Error : ", RFR_score_train)

# prediction on Test data
RFR_ts_predict = RFR.predict(X_test)

# R squared Error: Goodness of fit
RFR_score_test = metrics.r2_score(Y_test, RFR_ts_predict)
print("R squared Error : ", RFR_score_test)

"""# 5. Gradient Boosting Regressor"""

# loading the Random Forest Regressor model
GBR = GradientBoostingRegressor(n_estimators=50, learning_rate=0.1, max_depth=3)

GBR.fit(X_train,Y_train)

# prediction on Training data
GBR_tn_predict = GBR.predict(X_train)

# R squared Error: Goodness of fit
GBR_score_train = metrics.r2_score(Y_train, GBR_tn_predict)
print("R squared Error : ", GBR_score_train)

# prediction on Test data
GBR_ts_predict = GBR.predict(X_test)

# R squared Error: Goodness of fit
GBR_score_test = metrics.r2_score(Y_test, GBR_ts_predict)
print("R squared Error : ", GBR_score_test)

y_pred1 = LR.predict(X_test)
y_pred2 = LS.predict(X_test)
y_pred3 = DTR.predict(X_test)
y_pred4 = RFR.predict(X_test)
y_pred5 = GBR.predict(X_test)

df_pred = pd.DataFrame({"Actual": Y_test, 'LR': y_pred1, 'LS': y_pred2, 'DTR': y_pred3, 'RFR': y_pred4, 'GBR': y_pred5})

df_pred.sample(10)

## Mean Absolute Error: Lower the value better is the model fit.

MAE_1 = metrics.mean_absolute_error(Y_test, y_pred1)
MAE_2 = metrics.mean_absolute_error(Y_test, y_pred2)
MAE_3 = metrics.mean_absolute_error(Y_test, y_pred3)
MAE_4 = metrics.mean_absolute_error(Y_test, y_pred4)
MAE_5 = metrics.mean_absolute_error(Y_test, y_pred5)

print(MAE_1,MAE_2,MAE_3,MAE_4,MAE_5)

"""# Prediction on Random Data of the Person"""

# Lets take a random data for prediction

data = {"age": 45, "gender": 0, "BMI": 15, "Children": 1, "smoking_status": 1, "location": 3}
data

df_new = pd.DataFrame(data, index = [0])
df_new

## Predict health_insurance_price on above data using the best fit model from the above study. 
## Gradient Boosting Regressor gives the best results on the train and testing data set, hence it will be used for future predictions.

new_pred = GBR.predict(df_new)
new_pred

print("The Health Insurance Cost for the person will be: ", round(float(new_pred), 2),"/-")

################################################################################ End of the Report #####################################################################################