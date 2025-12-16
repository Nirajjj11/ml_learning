# Data set for people, Area in sq feet , age, income by using multiple regression predict the rent by input require area , age and income of the people.

#   Dataset id "rent.csv"

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("supervised_learning/data/rent.csv")

print(df)
X = df.drop(columns='rent')
# print(X)
y = df['rent']

model = LinearRegression()
model.fit(X,y)

area = int(input("Required Area in sq feet : "))
age = int(input("Enter age of the people : "))
income = int(input("Enter income of the people : "))

# predict_rent = model.predict([[area,age,income]])             # for directly use no need to input_df but for standard


input_df = pd.DataFrame({
    'area': [area],
    'age': [age],
    'income':[income]
})

predict_rent = model.predict(input_df)

print("Predicted Rent is : ",predict_rent[0])

print("Model Accuracy (R²):", model.score(X, y))
