# Day 095: Reduced-Order Modeling for Geotechnics

## Phase: Geotechnical AI Capstone Projects

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Reduced-order modeling (ROM) concepts and motivation
- Proper Orthogonal Decomposition (POD) for dimensionality reduction
- Neural network-based surrogate models for FEM simulations
- Training surrogates on FEM simulation databases
- Speed-accuracy tradeoffs in reduced-order geotechnical models

## Key Takeaways

1. Reduced-order models approximate expensive FEM simulations at a fraction of the computational cost.
2. POD extracts the dominant modes of variation from simulation databases, enabling efficient low-dimensional representations.
3. Neural network surrogates trained on FEM databases enable real-time predictions for design optimization and uncertainty quantification.

## Code Summary

- Built a neural network surrogate for a geotechnical FEM problem, trained on simulation data, and benchmarked speed vs. accuracy against full FEM

## Geotechnical Application

- Replacing expensive finite element simulations with fast ML surrogates for geotechnical design optimization and probabilistic analysis

## Resources

- [Reduced-Order Modeling — Benner et al.](https://doi.org/10.1137/1.9781611974829)
- [Neural Network Surrogates for Engineering — Review](https://www.sciencedirect.com/)

---

> *Day 095 of 100 — 100 Days of ML for Geotechnical Engineering*
