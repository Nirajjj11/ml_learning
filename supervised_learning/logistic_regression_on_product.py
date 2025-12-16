#  Q1. Load data set using pandas.
#  Q2. Prepare a model for feedback_rate & state of product using logistic regression model.
#  Q3. Take user Input product Name, feedback then predict the success / failure state of the product.
#  Q4. Also compute the accuracy of percent of the model after the predictions.

# Data Set is "product.csv" in data dir.

from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Q2: Load dataset
df = pd.read_csv("supervised_learning/data/product.csv")

# Q2: Prepare model
X = df[['feedback_rate']]
y = df['state']

X_train, X_test , y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression()
model.fit(X_train,y_train)

# Q3: User Input
product = input("Enter the product : ")
feedback = float(input("Enter feedback 0-5 : "))

prediction = model.predict([[feedback]])

# print("State of the product : ",prediction[0])

state = "Success" if prediction[0] == 1 else "Failure"
print(f"State od the Product '{product}' : {state}")

# print("Accuracy rate : ", accuracy_score(y_test,success[0]*100))      # not working


# Q4: Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred) * 100
print("Accuracy rate:", accuracy, "%")



