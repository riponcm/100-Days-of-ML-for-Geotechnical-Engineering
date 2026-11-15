# Day 048: Cross-Validation & Hyperparameter Tuning

## Phase: Classical Machine Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- K-fold cross-validation and stratified K-fold
- Leave-one-out and repeated cross-validation
- Hyperparameter tuning concepts and search spaces
- Overfitting detection through train vs. validation curves
- Nested cross-validation for unbiased performance estimation

## Key Takeaways

1. Cross-validation provides a more reliable performance estimate than a single train-test split, especially with small geotechnical datasets.
2. Stratified K-fold preserves class proportions in each fold, important when soil type frequencies are unequal.
3. Nested cross-validation separates model selection from performance evaluation to avoid optimistic bias.

## Code Summary

- Implemented K-fold and stratified cross-validation for geotechnical models, plotted learning and validation curves, and demonstrated nested CV

## Geotechnical Application

- Reliably estimating model performance on limited geotechnical datasets and selecting optimal model configurations

## Resources

- [Scikit-Learn Cross-Validation](https://scikit-learn.org/stable/modules/cross_validation.html)
- [Cross-Validation Strategies](https://scikit-learn.org/stable/auto_examples/model_selection/)

---

> *Day 048 of 100 — 100 Days of ML for Geotechnical Engineering*
