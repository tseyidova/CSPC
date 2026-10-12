import pandas as pd

# Load the data
ch = pd.read_csv("chemicals_cancer.csv")

# Inspect the structure
print(ch.shape)
print(ch.columns.tolist())
print(ch.head())
print(ch.describe())