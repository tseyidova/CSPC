# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup

Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**

- A radioactive decay simulation with two implementations (pure-Python loop and vectorised NumPy), tested with pytest, and a speed comparison script.

**Speed comparison (loop vs NumPy):**

- loop : 2.0864 s
- numpy : 0.0002 s
- speed-up: 12350.5x faster

**Tests:** all passing? yes

**Conclusion:**

- The NumPy vectorised version is dramatically faster than the pure-Python loop because it processes all atoms at once instead of looping over each one individually. All three tests pass, confirming the simulation correctly rejects negative decay rates and matches the theoretical decay law on average.
