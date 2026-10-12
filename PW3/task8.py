import numpy as np
import pandas as pd

# Load the data
df = pd.read_csv("heart.csv")

# Shannon entropy of a categorical column (in bits)
for col in ["target", "sex"]:
    p = df[col].value_counts(normalize=True)
    entropy = -(p * np.log2(p)).sum()
    max_entropy = np.log2(len(p))
    print(f"{col}: proportions = {p.round(3).to_dict()}")
    print(f"  entropy = {entropy:.3f} bits (max = {max_entropy:.3f}), "
          f"normalized = {entropy / max_entropy:.3f}")