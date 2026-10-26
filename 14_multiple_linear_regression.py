# Experiment 14: Multiple Linear Regression
import numpy as np
from sklearn.linear_model import LinearRegression

# Features: hours studied and hours slept
X = np.array([
    [1, 6], [2, 7], [3, 6], [4, 8], [5, 7], [6, 8]
])
y = np.array([35, 42, 50, 58, 65, 75])

model = LinearRegression()
model.fit(X, y)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Predicted marks:", model.predict([[5, 8]])[0])
