# Day 027: SciPy — Optimization

## Phase: Data Science Essentials

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Scalar optimization with scipy.optimize.minimize_scalar
- Multivariate optimization with scipy.optimize.minimize (Nelder-Mead, BFGS, L-BFGS-B)
- Constrained optimization with bounds and constraints
- Root finding with scipy.optimize.root and brentq
- Least-squares fitting with scipy.optimize.least_squares

## Key Takeaways

1. Optimization algorithms are essential for calibrating constitutive model parameters to match experimental soil behavior.
2. Constrained optimization ensures that fitted parameters remain physically meaningful (e.g., positive friction angles, bounded cohesion).
3. Choosing the right optimizer depends on the problem structure: gradient-based for smooth problems, Nelder-Mead for noisy objectives.

## Code Summary

- Calibrated Mohr-Coulomb parameters by minimizing error, used constrained optimization to fit a soil-water characteristic curve, and optimized a slope stability factor of safety

## Geotechnical Application

- Calibrating soil constitutive model parameters from laboratory test data and optimizing geotechnical design variables

## Resources

- [SciPy Optimization Documentation](https://docs.scipy.org/doc/scipy/reference/optimize.html)
- [SciPy Optimize Tutorial](https://docs.scipy.org/doc/scipy/tutorial/optimize.html)

---

> *Day 027 of 100 — 100 Days of ML for Geotechnical Engineering*
