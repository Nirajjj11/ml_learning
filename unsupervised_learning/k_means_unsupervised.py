# Q1. Load the dtaa set & create DF
# Q2. Create three Cluster
# Q3. plot a diagram for 3-Cluster

# Dataset used : "unsupervised_learning/data/people_income.csv"

import pandas as pd

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("unsupervised_learning/data/people_income.csv")
# print(df)
X = df[['annual_income', 'spending_score']]
# print(X)
model = KMeans(n_clusters=3,random_state=0)
model.fit(X)

df['cluster']= model.labels_
# print(df)

plt.scatter(X['annual_income'],X['spending_score'], c=df['cluster'])

plt.title("Spending Score vs Annual Income")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")

plt.show()