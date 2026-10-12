import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load the data
df = pd.read_csv("heart.csv")
cont = ["age", "chol", "trestbps", "thalach"]

# QQ-plots: points on the red line mean "approximately normal"
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, col in zip(axes.ravel(), cont):
    stats.probplot(df[col], dist="norm", plot=ax)
    ax.set_title(f"QQ-plot: {col}")
plt.tight_layout()
plt.savefig("qqplots.png", dpi=150)
plt.show()

# Shapiro-Wilk test: p > 0.05 -> cannot reject normality
for col in cont:
    w, p = stats.shapiro(df[col])
    skew = stats.skew(df[col])
    print(f"{col}: W = {w:.4f}, p = {p:.4g}, skewness = {skew:.2f}")