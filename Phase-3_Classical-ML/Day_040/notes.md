# Day 040: K-Nearest Neighbors (KNN)

## Phase: Classical Machine Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- KNN algorithm: distance-based classification and regression
- Choosing K and its effect on bias-variance tradeoff
- Distance metrics: Euclidean, Manhattan, Minkowski
- Feature scaling requirements for distance-based methods
- KNN strengths and limitations

## Key Takeaways

1. KNN makes predictions based on similar historical cases, aligning with how geotechnical engineers use precedent and experience.
2. Feature scaling is critical for KNN because unscaled features with larger ranges dominate the distance calculation.
3. KNN is intuitive but becomes slow on large datasets and sensitive to irrelevant features.

## Code Summary

- Implemented KNN for soil type classification from index properties, explored the effect of K on accuracy, and visualized decision boundaries in 2D

## Geotechnical Application

- Classifying soil types by finding the most similar historical samples based on measured index properties

## Resources

- [Scikit-Learn KNN](https://scikit-learn.org/stable/modules/neighbors.html)
- [KNN Algorithm Explained](https://towardsdatascience.com/)

---

> *Day 040 of 100 — 100 Days of ML for Geotechnical Engineering*
