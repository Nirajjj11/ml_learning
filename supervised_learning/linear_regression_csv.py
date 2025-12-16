import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("supervised_learning/data/room.csv")       # Data set is "room.csv"

# area = df['area']
# rent = df['rent']

# print('Area', area)
# print('Rent', rent)

X = df[['area']]
y = df['rent']

model = LinearRegression()
model.fit(X, y)

input_area = int(input("Enter the area : "))

predicted_rent = model.predict([[input_area]])

print("Predicted Price is : ",predicted_rent[0])