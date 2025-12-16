import matplotlib.pyplot  as plt

X = [1,2,3,4,5,6,7,8,9,10]
y = [0,0,0,0,0,1,1,1,1,1]

plt.title('Sigmoid function ')
plt.plot(X,y)
plt.xlabel("Hours of Work")
plt.ylabel("Sigmoid Value")
plt.show()