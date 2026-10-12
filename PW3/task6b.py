import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load the data
ch = pd.read_csv("chemicals_cancer.csv")

# Naive analysis: correlation of each chemical with malignancy
for chem in ["benzene", "cadmium"]:
    r, p_r = stats.pearsonr(ch[chem], ch["malignancy"])
    rho, p_rho = stats.spearmanr(ch[chem], ch["malignancy"])
    print(f"{chem}: Pearson r = {r:.3f} (p = {p_r:.3g}), "
          f"Spearman rho = {rho:.3f} (p = {p_rho:.3g})")

# Scatter plots: chemical vs malignancy
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, chem in zip(axes, ["benzene", "cadmium"]):
    ax.scatter(ch[chem], ch["malignancy"], alpha=0.4)
    ax.set_xlabel(chem)
    ax.set_ylabel("malignancy")
    ax.set_title(f"{chem} vs malignancy")
plt.tight_layout()
plt.savefig("naive_scatter.png", dpi=150)