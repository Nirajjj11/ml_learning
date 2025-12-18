#  Q. Draw a dendrogram for the point in the dataset

# Dataset for the program is : "unsupervised_learning\data\points_data_set.csv"

# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering

df = pd.read_csv("unsupervised_learning/data/points_data_set.csv")
print(df)
df2 = df.drop('point', axis=1)
print(df2)
X = pd.DataFrame(df2)

# print(X)

plt.figure(figsize=(8,5))
linked = linkage(X, method='ward')
dendrogram(linked,orientation='top', distance_sort='descending', show_leaf_counts = True )
plt.title("Hierarchical Cluster")
plt.show()