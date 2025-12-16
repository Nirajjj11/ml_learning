# Linear Regression - using numpy.array

import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1000],[1200],[700],[650],[1800],[2000]])
y = np.array([4000,4500,3500,2500,5500,5300])

model = LinearRegression()
model.fit(x,y)

area = int(input("Enter the area for rent : "))
price = model.predict([[area]])
print("For Area in sq.fit : ",area,",Rent is : ", price[0])
