# -*- coding: utf-8 -*-
"""lvadsusr174_poovisha_sabapathi_regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jKpl9xX1ME2X33hNsmXh6p29xbLN4e60
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder,PolynomialFeatures, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score

df=pd.read_csv('/content/Fare prediction.csv')
df

df.info()

np.size(df)

np.shape(df)

df.describe()

for column in df.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure(figsize=(10, 5))
    sns.histplot(df[column])
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

for column in df.select_dtypes(include=['float64', 'int64']).columns:
    plt.figure(figsize=(10, 5))
    sns.histplot(df[column])
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

df.isnull().sum()

df.duplicated().sum()

numerical_cols=df.select_dtypes(include=['int64','float64'])
corr_mat=numerical_cols.corr()
plt.figure(figsize=(15,7))
sns.heatmap(corr_mat,annot=True)

df=pd.to_datetime(df['pickup_datetime'])

df.info()

def object_to_int(x):
  if x.dtype=='object':
    x=LabelEncoder().fit_transform(x)
  return x

df=df.apply(lambda x: object_to_int(x))
df.head(20)

df.info()

X=df.drop(columns=['fare_amount'])
y=df['fare_amount'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4)

poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_poly)
X_test_scaled = scaler.transform(X_test_poly)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions, squared=False)
r2 = r2_score(y_test, predictions)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

print('Mean Absolute Error (MAE):', mae)
print('Mean Squared Error (MSE):', mse)
print('Root Mean Squared Error (RMSE):', rmse)
print('R-squared (R2) Score:', r2)