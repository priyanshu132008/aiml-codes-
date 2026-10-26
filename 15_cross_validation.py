# Experiment 15: Calculate cross-validation score on Iris dataset
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score

data = load_iris()
model = DecisionTreeClassifier(random_state=42)

scores = cross_val_score(model, data.data, data.target, cv=5)
print("Cross-validation scores:", scores)
print("Mean score:", scores.mean())
