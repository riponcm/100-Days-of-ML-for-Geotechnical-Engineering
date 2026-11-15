# Day 031: Feature Engineering Techniques

## Phase: Data Science Essentials

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Creating new features from domain knowledge (ratios, interactions, polynomial terms)
- Encoding categorical variables: one-hot, ordinal, target encoding
- Binning and discretization of continuous variables
- Log and power transformations for skewed distributions
- Feature scaling: standardization, min-max normalization, robust scaling

## Key Takeaways

1. Domain-specific features like the plasticity index (LL - PL) or overburden stress ratio often outperform raw measurements in ML models.
2. Proper encoding of soil classification categories is essential for algorithms that require numerical inputs.
3. Feature scaling ensures that parameters on different scales contribute equally to distance-based models.

## Code Summary

- Engineered geotechnical features (liquefaction index, normalized SPT, overburden corrections), applied encoding to soil types, and compared model performance with and without engineered features

## Geotechnical Application

- Creating physically meaningful features from raw site investigation data to improve ML model predictions for soil behavior

## Resources

- [Feature Engineering for Machine Learning (Alice Zheng)](https://www.oreilly.com/library/view/feature-engineering-for/9781491953235/)
- [Scikit-Learn Preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)

---

> *Day 031 of 100 — 100 Days of ML for Geotechnical Engineering*
