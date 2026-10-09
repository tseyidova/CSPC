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

---

## PW1 - Lab B: Data, Plotting, and Automation

**What the data showed:**

- The observed decay data (decay_observed.csv) shows the atom count dropping from 5000 at t=0 down toward near-zero by t=20, following the expected shape of radioactive decay.

**Did it match the analytical law?**

- Yes, comparing the two panels of figure.png, the observed scatter points closely follow the same shape as the analytical curve N0*exp(-lam*t), confirming the data is consistent with the decay law (lambda = 0.3).

**Snakemake pipeline:**

- The Snakefile defines one rule that regenerates figure.png from decay_observed.csv by running plot_STUDENT.py, and Snakemake only reruns it when the input file is newer than the output, avoiding unnecessary recomputation.

---

## PW2 - Lab B: Optimization in Chemistry

**How the three methods compared:**

- On f(x) = (x-3)^2 + 1, gradient descent, Newton and SLSQP all gave x = 3.
- On g(x) = x^4 - 3x^2 + x + 5, the results depended on the start. From x0=0, Newton landed on x = 0.17, where g'' < 0, so it is a maximum. From x0=2, gradient descent and Newton stopped at the local minimum x = 1.13, while SLSQP reached the lowest point x = -1.30.
- So the methods only agree on the easy problem. On the harder one, the starting point and the method both change the answer.

**Fitted rate constant:**

- The fit gave k = 0.262, close to the expected 0.25. The difference comes from noise in the data.

**Equilibrium composition:**

- Newton and SLSQP agree: x = 0.664, giving H2 = I2 = 0.336 mol and HI = 1.328 mol.

**Titration equivalence point:**

- The pH curve is steepest at 50.0 mL, so that is the equivalence point.
