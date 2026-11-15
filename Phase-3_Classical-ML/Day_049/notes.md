# Day 049: Grid Search vs Random Search vs Optuna

## Phase: Classical Machine Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Grid search: exhaustive hyperparameter exploration
- Random search: efficient sampling of hyperparameter space
- Optuna: Bayesian optimization with Tree-structured Parzen Estimators
- Search space definition and pruning strategies
- Comparing search efficiency and final model performance

## Key Takeaways

1. Random search is often more efficient than grid search because it explores the hyperparameter space more broadly.
2. Optuna uses Bayesian optimization to intelligently focus search on promising hyperparameter regions, saving computation time.
3. Proper hyperparameter tuning can significantly improve model performance on geotechnical prediction tasks.

## Code Summary

- Compared grid search, random search, and Optuna on an XGBoost model, visualized hyperparameter importance, and analyzed search efficiency

## Geotechnical Application

- Efficiently finding the best model configuration for geotechnical predictions when computational resources and data are limited

## Resources

- [Optuna Documentation](https://optuna.readthedocs.io/)
- [Scikit-Learn GridSearchCV](https://scikit-learn.org/stable/modules/grid_search.html)

---

> *Day 049 of 100 — 100 Days of ML for Geotechnical Engineering*
