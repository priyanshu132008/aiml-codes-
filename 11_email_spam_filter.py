# Experiment 11: Email spam and non-spam filtering using ML
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

emails = [
    "Win money now", "Claim your free prize",
    "Meeting is at ten", "Please send the assignment",
    "Free offer click now", "See you in class"
]
labels = ["spam", "spam", "not spam", "not spam", "spam", "not spam"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)
model = MultinomialNB()
model.fit(X, labels)

message = input("Enter an email message: ")
prediction = model.predict(vectorizer.transform([message]))
print("Email category:", prediction[0])
