# Day 038: Polynomial, Ridge & Lasso Regression

## Phase: Classical Machine Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Polynomial feature expansion for nonlinear relationships
- Overfitting and the bias-variance tradeoff
- Ridge regression (L2 regularization) to reduce overfitting
- Lasso regression (L1 regularization) for feature selection
- Elastic Net combining L1 and L2 penalties

## Key Takeaways

1. Many geotechnical relationships (e.g., SPT-N vs. depth) are nonlinear, making polynomial features or regularized models necessary.
2. Ridge regression shrinks coefficients uniformly, while Lasso can drive irrelevant features to exactly zero, performing automatic feature selection.
3. Cross-validation is essential for selecting the regularization strength that balances fit quality and model complexity.

## Code Summary

- Compared linear, polynomial, Ridge, and Lasso models on a geotechnical dataset, visualized overfitting with polynomial degree, and demonstrated Lasso feature selection

## Geotechnical Application

- Modeling nonlinear soil property correlations while preventing overfitting on limited geotechnical datasets

## Resources

- [Scikit-Learn Ridge and Lasso](https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression)
- [Regularization in Machine Learning](https://towardsdatascience.com/)

---

> *Day 038 of 100 — 100 Days of ML for Geotechnical Engineering*
