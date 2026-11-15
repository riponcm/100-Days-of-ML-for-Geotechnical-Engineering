# Day 056: Shear Wave Velocity from SPT (ML)

## Phase: Classical Machine Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Shear wave velocity (Vs) and its importance in geotechnical engineering
- Traditional SPT-Vs empirical correlations and their limitations
- Feature selection for Vs prediction (N-value, depth, soil type, fines content)
- Regression model comparison: linear, polynomial, Random Forest, XGBoost
- Model validation against measured Vs data

## Key Takeaways

1. Vs is a fundamental parameter for site response analysis and soil classification, but direct measurement is expensive.
2. ML models can predict Vs from readily available SPT data more accurately than simple empirical correlations.
3. Including soil type and depth as features alongside SPT-N significantly improves Vs prediction accuracy.

## Code Summary

- Trained regression models to predict Vs from SPT data, compared ML performance with traditional correlations, and validated on independent test sets

## Geotechnical Application

- Estimating shear wave velocity from Standard Penetration Test results when direct measurements (MASW, downhole, crosshole) are not available

## Resources

- [Correlation Between SPT-N and Vs — Literature Review](https://www.sciencedirect.com/)
- [Scikit-Learn Regression Models](https://scikit-learn.org/stable/supervised_learning.html)

---

> *Day 056 of 100 — 100 Days of ML for Geotechnical Engineering*
