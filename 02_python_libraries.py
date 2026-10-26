# Experiment 2: Use NumPy, Pandas and Matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

numbers = np.array([10, 20, 30, 40, 50])
print("NumPy array:", numbers)
print("Mean:", np.mean(numbers))

df = pd.DataFrame({"Name": ["Asha", "Ravi", "Neha"], "Marks": [80, 75, 92]})
print(df)
print(df.describe())

df.plot(x="Name", y="Marks", kind="bar")
plt.tight_layout()
plt.show()
