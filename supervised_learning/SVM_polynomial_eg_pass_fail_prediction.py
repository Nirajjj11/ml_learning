# Take user input as - hours and marks and predict the success / Failure in competition using SVM polynomial kernel function

# Dataset used : "result.csv"

import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split

df = pd.read_csv('supervised_learning/data/result.csv')

# print(df)

# X = df[['hours', 'marks']]            # we can use it as well instead of below
X = df.drop('pass', axis=1)
# print(X)
y = df['pass']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=42)

model = svm.SVC(kernel='poly',degree=3,C= 1.0, gamma='scale')
model.fit(X_train,y_train)

hours = int(input("Enter Exact Study Hours : "))
marks = int(input("Enter Obtained Marks : "))

input_df = pd.DataFrame([[hours,marks]], columns=X.columns)

pred = model.predict(input_df)

if pred[0] == 1:
    print("Pass :)")
else:
    print("Fail :( ")