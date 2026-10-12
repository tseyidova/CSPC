import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load the data
df = pd.read_csv("heart.csv")

# Quantify the relationship
r, p_r = stats.pearsonr(df["age"], df["thalach"])
rho, p_rho = stats.spearmanr(df["age"], df["thalach"])
print(f"Pearson r = {r:.3f}, p = {p_r:.3g}")
print(f"Spearman rho = {rho:.3f}, p = {p_rho:.3g}")

# Linear fit for the trend line
slope, intercept = np.polyfit(df["age"], df["thalach"], 1)
print(f"Slope = {slope:.3f} bpm per year")

# Scatter plot with trend line
plt.figure(figsize=(6, 5))
plt.scatter(df["age"], df["thalach"], alpha=0.6)
xs = np.linspace(df["age"].min(), df["age"].max(), 100)
plt.plot(xs, slope * xs + intercept, color="red")
plt.xlabel("age (years)")
plt.ylabel("thalach (bpm)")
plt.title("Age vs max heart rate")
plt.savefig("age_thalach.png", dpi=150)
plt.show()