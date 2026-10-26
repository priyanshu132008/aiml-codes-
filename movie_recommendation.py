import pandas as pd

# Create a small dataset
data = {
    "Movie": ["Inception", "Interstellar", "The Notebook",
              "Titanic", "Avengers", "Iron Man"],
    "Genre": ["Sci-Fi", "Sci-Fi", "Romance",
              "Romance", "Action", "Action"]
}

df = pd.DataFrame(data)

print("Available Movies:")
print(df)

genre = input("Enter your favourite genre: ").title()

recommended = df[df["Genre"] == genre]

print("\nRecommended Movies:")
if len(recommended) > 0:
    print(recommended["Movie"].to_string(index=False))
else:
    print("No movies found for this genre.")
