# Day 050: Regression Metrics (R-squared, RMSE, MAE)

## Phase: Classical Machine Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- R-squared (coefficient of determination) and adjusted R-squared
- Root Mean Squared Error (RMSE) and Mean Absolute Error (MAE)
- Mean Absolute Percentage Error (MAPE) for scale-independent comparison
- Residual analysis and prediction interval estimation
- Choosing metrics based on the engineering use case

## Key Takeaways

1. RMSE penalizes large errors more heavily, which is appropriate when large prediction errors have disproportionate engineering consequences.
2. MAE is more robust to outliers and gives equal weight to all errors, suitable when occasional large deviations are acceptable.
3. No single metric tells the whole story; combining R-squared with RMSE and residual plots provides a complete evaluation.

## Code Summary

- Evaluated regression models using multiple metrics, demonstrated how different metrics rank models differently, and built prediction interval plots

## Geotechnical Application

- Quantifying the accuracy of ML predictions for geotechnical parameters and communicating prediction uncertainty to engineering teams

## Resources

- [Scikit-Learn Regression Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics)
- [Understanding R-squared — StatQuest](https://www.youtube.com/watch?v=2AQKmw14mHM)

---

> *Day 050 of 100 — 100 Days of ML for Geotechnical Engineering*
