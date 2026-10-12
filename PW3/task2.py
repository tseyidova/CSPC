import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("heart.csv")
cont = ["age", "chol", "trestbps", "thalach"]

# One figure with four histogram panels
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, col in zip(axes.ravel(), cont):
    ax.hist(df[col], bins=20, edgecolor="black")
    ax.set_title(col)
    ax.set_xlabel(col)
    ax.set_ylabel("count")

plt.tight_layout()
plt.savefig("distributions.png", dpi=150)
plt.show()