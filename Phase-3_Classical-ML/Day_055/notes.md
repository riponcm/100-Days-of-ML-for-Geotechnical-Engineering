# Day 055: Soil Liquefaction Prediction (ML)

## Phase: Classical Machine Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Liquefaction triggering criteria and key input parameters
- Feature engineering for liquefaction prediction (CSR, CRR, SPT corrections)
- Comparing classifiers: logistic regression, Random Forest, XGBoost
- Model evaluation with emphasis on recall (minimizing missed failures)
- Comparison with traditional empirical methods (Seed & Idriss, Boulanger & Idriss)

## Key Takeaways

1. ML models can capture nonlinear interactions between liquefaction factors that simplified empirical charts cannot represent.
2. Recall is the critical metric for liquefaction prediction because failing to predict liquefaction has severe consequences.
3. ML-based predictions should be validated against established empirical methods and engineering judgment.

## Code Summary

- Built and compared multiple ML classifiers for liquefaction prediction, evaluated against empirical charts, and analyzed feature importance for physical consistency

## Geotechnical Application

- Predicting soil liquefaction potential during earthquakes using machine learning trained on historical case histories

## Resources

- [Boulanger & Idriss (2014) — SPT Liquefaction Triggering](https://doi.org/10.1061/(ASCE)GT.1943-5606.0001388)
- [ML for Liquefaction — Recent Advances](https://www.sciencedirect.com/)

---

> *Day 055 of 100 — 100 Days of ML for Geotechnical Engineering*
