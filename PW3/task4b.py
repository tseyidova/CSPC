import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load the data
df = pd.read_csv("heart.csv")
disease = df.loc[df["target"] == 1, "thalach"]
healthy = df.loc[df["target"] == 0, "thalach"]

# Mean, standard error of the mean (SEM) and 95% confidence interval
names, means, cis = [], [], []
for name, g in [("disease", disease), ("healthy", healthy)]:
    mean = g.mean()
    sem = stats.sem(g)
    ci95 = 1.96 * sem
    print(f"{name}: mean = {mean:.2f}, SEM = {sem:.2f}, "
          f"95% CI = [{mean - ci95:.2f}, {mean + ci95:.2f}], n = {len(g)}")
    names.append(name)
    means.append(mean)
    cis.append(ci95)

# Plot the two means with 95% CI error bars
plt.figure(figsize=(5, 5))
plt.errorbar(names, means, yerr=cis, fmt="o", capsize=8, markersize=8)
plt.ylabel("mean thalach (bpm), 95% CI")
plt.title("Max heart rate by group")
plt.savefig("thalach_means.png", dpi=150)
plt.show()