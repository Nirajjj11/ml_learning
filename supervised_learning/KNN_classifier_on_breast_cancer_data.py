from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt 


cancer = load_breast_cancer()

X_train, X_test, y_train , y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=66)

tranning_accuracy = []
test_accuracy = []

# try n_neighbors from 1 to 11

neighbors_setting  = range(1,11)
for n_neighbors in neighbors_setting:
    # built the model
    clf = KNeighborsClassifier(n_neighbors=n_neighbors)
    clf.fit(X_train,y_train)

    # record the training set accuracy
    tranning_accuracy.append(clf.score(X_train, y_train))

    # record the generalization accuracy 
    test_accuracy.append(clf.score(X_test, y_test))

# now Plotting 

plt.plot(neighbors_setting, tranning_accuracy,label="tranning_accuracy")
plt.plot(neighbors_setting, test_accuracy, label="test_accuracy") 
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.show()
