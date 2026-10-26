import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Create sample dataset
data = {
    "Income": [25000, 30000, 60000, 80000, 20000, 70000, 45000, 90000],
    "CreditScore": [550, 600, 750, 800, 500, 720, 680, 820],
    "Approved": [0, 0, 1, 1, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Income", "CreditScore"]]
y = df["Approved"]

# Train model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Get applicant details
income = float(input("Enter monthly income: "))
score = int(input("Enter credit score: "))

prediction = model.predict([[income, score]])

if prediction[0] == 1:
    print("Predicted result: Loan Approved")
else:
    print("Predicted result: Loan Not Approved")
