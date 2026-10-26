# Experiment 8: Find, load and explore a dataset
# This uses the built-in Iris dataset, so no download is needed.
from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

iris = load_iris(as_frame=True)
df = iris.frame

print("Dataset: Iris")
print("Dataset source: https://scikit-learn.org/stable/datasets/toy_dataset.html#iris-plants-dataset")
print(df.head())
print("Shape:", df.shape)
print(df.info())
print(df.describe())
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()
df.hist(figsize=(8, 6))
plt.tight_layout()
plt.show()
