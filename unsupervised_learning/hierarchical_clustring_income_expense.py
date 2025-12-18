#  Q. Draw a dendrogram and show the income/ expense alternaive hierarchy.

# Data set is used is : "unsupervised_learning\data\hierarchical_clustring_income_expense.csv"

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

df = pd.read_csv("unsupervised_learning/data/hierarchical_clustring_income_expense.csv")
# print(df)

df1 = df [['income', 'expense']]
# print(df1)
X = np.array(df)
# print(X)

plt.figure(figsize=(8,5))
linked = linkage(X, method='ward')
dendrogram(linked, orientation='top', show_leaf_counts=True)
plt.xlabel("Data Merge Point")
plt.ylabel("Difference Income and Expense")
plt.title("Organization Income / Expense Dendrogram")

plt.show()