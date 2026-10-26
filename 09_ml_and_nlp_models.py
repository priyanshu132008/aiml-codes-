# Experiment 9: Build an ML model and an NLP model
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# ML model: Iris classification
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("Iris model accuracy:", accuracy_score(y_test, pred))

# NLP model: spam classification
texts = [
    "Win a free prize now", "Claim your free reward",
    "Hello how are you", "Please send the notes",
    "You won a free gift", "Let's meet tomorrow"
]
labels = ["spam", "spam", "ham", "ham", "spam", "ham"]
vectorizer = TfidfVectorizer()
text_features = vectorizer.fit_transform(texts)
nlp_model = MultinomialNB()
nlp_model.fit(text_features, labels)
new_message = vectorizer.transform(["Win a free gift"])
print("Text prediction:", nlp_model.predict(new_message)[0])
