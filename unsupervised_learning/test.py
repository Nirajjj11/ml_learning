import matplotlib.pyplot as plt

X = [2, 3, 1, 5]
Y = [3, 4, 1, 6]


import pandas as pd

df = pd.DataFrame({
    'x': [2,3,1,5],
    'y': [3,4,1,6]
})

ax = df.plot.scatter(x='x', y='y')
ax.set_title("Scatter Plot")



plt.show()   # 🔴 REQUIRED
