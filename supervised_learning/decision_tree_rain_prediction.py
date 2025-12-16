import pandas as pd
from sklearn import tree

df = pd.read_csv("supervised_learning/data/rain.csv")

# print(df)                 #   ->    Simply Print the data 

df_encode = df.apply(lambda col:col.astype('category').cat.codes)

# print(df_encode)          #   ->    Encode the value in numerical form

model = tree.DecisionTreeClassifier()
X = df_encode.drop('rain',axis=1)
y = df_encode['rain']

sky = input("Enter Sky : ").upper()
humidity = input("Enter humidity : ").upper()
temperture = input("Enter Temperature : ").upper()

feature =[]

if sky == "CLEAN":
    feature.append(0)
elif sky == "CLOUD":
    feature.append(1)

if humidity == "NO":
    feature.append(0)
elif humidity == "YES":
    feature.append(1)
else:
    feature.append(0)

if temperture == "MEDIUM":
    feature.append(2)
elif temperture == "HIGH":
    feature.append(0)
elif temperture == "LOW":
    feature.append(1)
else:
    feature.append(1)


model.fit(X,y)
print("Feature is : ",feature)
predict_rain = model.predict([feature])

if predict_rain[0] == 1:
    print("It will rain")
else:
    print("It will not rain ")