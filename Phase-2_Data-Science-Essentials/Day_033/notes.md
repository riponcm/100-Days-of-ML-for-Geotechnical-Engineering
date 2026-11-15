# Day 033: Handling Imbalanced Datasets

## Phase: Data Science Essentials

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Understanding class imbalance and its impact on model training
- Oversampling techniques: SMOTE, ADASYN, random oversampling
- Undersampling techniques: random undersampling, Tomek links
- Cost-sensitive learning with class weights
- Evaluation metrics suitable for imbalanced data (precision, recall, F1, AUC)

## Key Takeaways

1. Geotechnical failure datasets are inherently imbalanced because failures (e.g., liquefaction) are rare compared to stable conditions.
2. SMOTE generates synthetic minority samples that help the model learn decision boundaries without simply duplicating existing data.
3. Using accuracy alone on imbalanced datasets is misleading; precision-recall curves and F1 scores are more informative.

## Code Summary

- Demonstrated the effect of class imbalance on a soil liquefaction classifier, applied SMOTE and class weighting, and compared performance using confusion matrices and PR curves

## Geotechnical Application

- Addressing the scarcity of failure cases in geotechnical datasets when building classifiers for hazard prediction

## Resources

- [imbalanced-learn Documentation](https://imbalanced-learn.org/stable/)
- [SMOTE: Synthetic Minority Over-sampling Technique](https://arxiv.org/abs/1106.1813)

---

> *Day 033 of 100 — 100 Days of ML for Geotechnical Engineering*
