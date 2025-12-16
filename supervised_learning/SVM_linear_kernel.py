# Take user input as coordinates and find the class member using SVM Linear kernel function

from sklearn import svm
import matplotlib.pyplot as plt

X = [[2,3],[3,4],[1,1],[5,6],[6,7],[4,3],[6,8]]
y = [1,0,0,1,1,0,1]

model = svm.SVC(kernel='linear')
model.fit(X,y)

x1 = int(input("Enter x - coordinate : "))
y1 = int(input("Enter y - coordinate : "))

feature = []
feature.append(x1)
feature.append(y1)

predict = model.predict([feature])

print("Class purpose by model : ",predict[0])
for i, point in enumerate(X):
    if y[i] == 0:
        plt.scatter(point[0],point[1],marker = 'o',label="Class 0")
    else:
        plt.scatter(point[0],point[1], marker='s', label="Class 1")


plt.scatter(x1, y1, marker='x', s=100, label='User Input')

plt.title("Linear Scatter ")
plt.xlabel("X")
plt.ylabel("class")
plt.show()

