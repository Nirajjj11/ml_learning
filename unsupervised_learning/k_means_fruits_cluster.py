# Make a cluster of the fruits name on the basic of their sweetness and sourness

#   --------------------- Data set -------------------

            #     fruits  sweetness  sourness  class
            # 0    Mango         10         0      1
            # 1   Orange          5         5      0
            # 2    Guava          8         1      1
            # 3    Lemon          2         8      2
            # 4  Mausami          1        10      2
            # 5    Apple         10         0      1
            # 6   Grapes          6         4      1



import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    'fruits':['Mango','Orange',"Guava",'Lemon','Mausami','Apple',"Grapes"],
    'sweetness': [10,5,8,2,1,10,6],
    'sourness': [0,5,1,8,10,0,4],
    'class': [1,0,1,2,2,1,1]
}

df = pd.DataFrame(data)
# print(df)

X = df[['sweetness','class']]

model = KMeans(n_clusters=3,random_state=42)
model.fit(X)

df['cluster']= model.labels_

plt.scatter(X['sweetness'],X['class'] , c=df['cluster'])

for i in range(len(df)):
    plt.text(df['sweetness'][i] + 0.1,
            df['sourness'][i] + 0.1,
            df['fruits'][i])

plt.title("Sourness and Sweetness Class Cluster")
plt.xlabel("Sweetness")
plt.ylabel("Sourness")

# plt.show()

print(df)
