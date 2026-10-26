# Experiment 13: Simple Linear Regression
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # hours studied
y = np.array([35, 40, 50, 60, 70])            # marks

model = LinearRegression()
model.fit(X, y)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Predicted marks for 6 hours:", model.predict([[6]])[0])

plt.scatter(X, y)
plt.plot(X, model.predict(X))
plt.xlabel("Hours studied")
plt.ylabel("Marks")
plt.show()
