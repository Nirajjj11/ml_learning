#  Take user input task_hours by using logistic regression Check the status/ Failure

#           task_hrs : [15,18,25,23,28,24.5,40,35,32,0.5]
#           success  : [0,0,1,0,1,1,0,1,1,0]

from sklearn.linear_model import LogisticRegression
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = {
    'task_hrs': [15,18,25,23,28,24.5,40,25,32,0.5],
    "success":  [0,0,1,0,1,1,0,1,1,0]
}

df = pd.DataFrame(data)

X = df[['task_hrs']]
y = df['success']

#  split Data
X_train,X_trainin,y_train,y_test = train_test_split(X,y,train_size=0.3,random_state=42)

# train model
model = LogisticRegression()
model.fit(X_train,y_train)

task_hrs_input = float(input("Enter the task hrs : "))
success_predict = model.predict([[task_hrs_input]])
print("Predicted Output : ", success_predict[0])

# print("Accuracy Score : ",accuracy_score(X_trainin, success_predict[0]))          # Not Working 

y_pred = model.predict(X_trainin)
print("Accuracy Score :", accuracy_score(y_test, y_pred))

