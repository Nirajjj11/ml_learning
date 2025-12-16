#  Take user input as hours, attendence_percent, predict pass status using SVM kernel function RBF

# Dataset is : "student_attendance.csv"

from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm

df = pd.read_csv("supervised_learning/data/student_attendance.csv")

# print(df)

X = df[['hours','attendence_percent']]
y = df['pass']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=42)

model = svm.SVC(kernel='rbf')
model.fit(X_train,y_train)

hrs = float(input("Enter attended class hours : "))
attend_per = float(input("Enter attendence percent : "))

input_df = pd.DataFrame({
    'hours':[hrs],
    'attendence_percent':[attend_per]
})

pred = model.predict(input_df)

if pred[0] == 1:
    print("Pass")
else:
    print("Fail")

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)
print("Accuracy Score is : ", accuracy)



