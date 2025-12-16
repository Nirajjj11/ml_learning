#  Predict the Loan Status for buy car

# Data set is "loan.csv"

import pandas as pd 
from sklearn import tree

df = pd.read_csv("supervised_learning/data/loan.csv")

# print(df)             #   ->    Simply Print the data 

df_encode = df.apply(lambda col: col.astype('category').cat.codes)

# print(df_encode)      #   ->    Encode the value in numerical form 

X = df_encode.drop(columns='loan_buy_car')   
y = df_encode['loan_buy_car']

model = tree.DecisionTreeClassifier()
model.fit(X,y)

age = input("Enter Junior / Youth / Middle / Senior :").upper()
income = input("Enter Low / High : ").upper()
credit = input("Enter Bad / Fair / Excellent :").upper()

feature =[]

if age == 'JUNIOR':
    feature.append(0)
elif age == 'YOUTH':
    feature.append(3)
elif age == 'MIDDLE':
    feature.append(1)
elif age == 'SENIOR':
    feature.append(2)
else:
    feature.append(0)

if income == 'LOW':
    feature.append(1)
else:
    feature.append(0)

if credit == "BAD":
    feature.append(0)
elif credit == "FAIR":
    feature.append(2)
elif credit == "EXCELLENT":
    feature.append(1)
else:
    feature.append(0)

predict_loan = model.predict([feature])
print("Prediction is : ",predict_loan[0])

if predict_loan == 0:
    print("Loan Not Approved.")
else:
    print("Loan Approved.")
