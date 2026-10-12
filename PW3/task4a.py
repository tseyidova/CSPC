import pandas as pd
from scipy import stats

# Load the data
df = pd.read_csv("heart.csv")

# Split thalach into the two groups defined by target
disease = df.loc[df["target"] == 1, "thalach"]
healthy = df.loc[df["target"] == 0, "thalach"]
print("n disease:", len(disease), " n healthy:", len(healthy))

# Check normality inside each group
print("Shapiro disease p =", stats.shapiro(disease)[1])
print("Shapiro healthy p =", stats.shapiro(healthy)[1])

# Mann-Whitney U (main test, no normality needed)
u, p_u = stats.mannwhitneyu(disease, healthy, alternative="two-sided")
print(f"Mann-Whitney U = {u:.1f}, p = {p_u:.3g}")

# Welch t-test (robustness check)
t, p_t = stats.ttest_ind(disease, healthy, equal_var=False)
print(f"Welch t = {t:.3f}, p = {p_t:.3g}")

# Group medians and means for context
print("Medians:", disease.median(), healthy.median())
print("Means:", disease.mean(), healthy.mean())