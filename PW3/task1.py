import pandas as pd

# Load the data
df = pd.read_csv("heart.csv")

# Shape and first rows
print("Shape:", df.shape)
print(df.head())

# Isolate the four continuous columns
cont = df[["age", "chol", "trestbps", "thalach"]]
print(cont.head())