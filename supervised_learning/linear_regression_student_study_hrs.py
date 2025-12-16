# WAP to take 10 students study hrs and obtain marks using data frame and compute marks for given study hrs using Linear Regression

#       Study hrs : [2,3,5,4,6,7,8,6.5,7.5,8.5]
#       Marks     : [32,38,45,38,70,85,90,68,81,88]


import pandas as pd 
from sklearn.linear_model import LinearRegression

data = {
    'hours':[2,3,5,4,6,7,8,6.5,7.5,8.5],
    'marks':[32,38,45,38,70,85,90,68,81,88]
}

df = pd.DataFrame(data)

X = df[['hours']]
y = df['marks']

model = LinearRegression()
model.fit(X,y)

input_hrs = float(input("Enter Study Hours : "))
marks_predict = model.predict([[input_hrs]])
print("Predicted marks : ", marks_predict[0])
