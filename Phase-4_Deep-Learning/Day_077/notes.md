# Day 077: Physics-Informed Neural Networks (PINNs)

## Phase: Deep Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- PINNs concept: embedding physical laws into neural network loss functions
- Encoding differential equations as soft constraints
- Boundary and initial condition enforcement
- Training with combined data loss and physics loss
- Advantages of PINNs over purely data-driven models

## Key Takeaways

1. PINNs incorporate known physical laws directly into the training process, ensuring predictions are physically consistent.
2. Physics constraints act as regularizers, enabling accurate predictions even with very limited training data.
3. Combining data-driven learning with physics-based constraints produces models that generalize better to unseen conditions.

## Code Summary

- Implemented a PINN to solve a simple differential equation (1D consolidation), combined data loss with physics loss, and compared with data-only models

## Geotechnical Application

- Solving geotechnical PDEs (consolidation, seepage, wave propagation) using neural networks constrained by governing equations

## Resources

- [Physics-Informed Neural Networks — Raissi et al.](https://www.sciencedirect.com/science/article/pii/S0021999118307125)
- [DeepXDE Library](https://deepxde.readthedocs.io/)

---

> *Day 077 of 100 — 100 Days of ML for Geotechnical Engineering*
