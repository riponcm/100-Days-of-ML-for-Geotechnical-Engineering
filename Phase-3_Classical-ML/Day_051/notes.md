# Day 051: Classification Metrics (ROC, AUC, F1)

## Phase: Classical Machine Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Confusion matrix: TP, FP, TN, FN and their engineering meaning
- Precision, recall, and F1 score
- ROC curve and Area Under the Curve (AUC)
- Precision-Recall curves for imbalanced datasets
- Threshold selection based on engineering risk tolerance

## Key Takeaways

1. In geotechnical hazard classification, the cost of false negatives (missing a failure) is typically much higher than false positives.
2. The classification threshold should be adjusted based on the engineering risk tolerance, not fixed at 0.5.
3. AUC provides a threshold-independent measure of classifier quality, useful for comparing models across different operating points.

## Code Summary

- Built classifiers with detailed metric analysis, plotted ROC and PR curves, and demonstrated threshold optimization for a soil liquefaction classifier

## Geotechnical Application

- Evaluating hazard classifiers where the consequences of misclassification (e.g., undetected liquefaction) carry different engineering risks

## Resources

- [Scikit-Learn Classification Metrics](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)
- [ROC Curve Explained — Google ML Crash Course](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc)

---

> *Day 051 of 100 — 100 Days of ML for Geotechnical Engineering*
