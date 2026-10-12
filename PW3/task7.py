import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load the data
ch = pd.read_csv("chemicals_cancer.csv")

# Step 1: correlation matrix (is pollution_index linked to everything?)
print("Correlation matrix:")
print(ch.corr().round(3))

# Step 2: restrict to patients with similar pollution_index
for low, high in [(40, 60), (45, 55)]:
    sub = ch[(ch["pollution_index"] > low) & (ch["pollution_index"] < high)]
    print(f"\nRestricted to pollution_index in ({low}, {high}), n = {len(sub)}")
    for chem in ["benzene", "cadmium"]:
        r, p = stats.pearsonr(sub[chem], sub["malignancy"])
        print(f"  {chem}: r = {r:.3f}, p = {p:.3g}")

# Step 3: partial correlation (remove the linear effect of pollution_index)
def residuals(y, x):
    slope, intercept = np.polyfit(x, y, 1)
    return y - (slope * x + intercept)

print("\nPartial correlation (pollution_index removed):")
res_mal = residuals(ch["malignancy"].values, ch["pollution_index"].values)
for chem in ["benzene", "cadmium"]:
    res_chem = residuals(ch[chem].values, ch["pollution_index"].values)
    r, p = stats.pearsonr(res_chem, res_mal)
    print(f"  {chem}: r = {r:.3f}, p = {p:.3g}")

# Plot: restricted group, chemical vs malignancy
sub = ch[(ch["pollution_index"] > 40) & (ch["pollution_index"] < 60)]
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, chem in zip(axes, ["benzene", "cadmium"]):
    ax.scatter(sub[chem], sub["malignancy"], alpha=0.5)
    ax.set_xlabel(chem)
    ax.set_ylabel("malignancy")
    ax.set_title(f"{chem} (pollution_index 40-60)")
plt.tight_layout()
plt.savefig("controlled_scatter.png", dpi=150)