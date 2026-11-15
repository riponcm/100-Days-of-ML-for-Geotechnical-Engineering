# Day 034: Dimensionality Reduction (PCA, SVD)

## Phase: Data Science Essentials

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Principal Component Analysis (PCA): theory, computation, and interpretation
- Explained variance ratio and selecting the number of components
- SVD as the computational backbone of PCA
- Visualizing high-dimensional data in 2D/3D using PCA projections
- t-SNE and UMAP for nonlinear dimensionality reduction

## Key Takeaways

1. PCA identifies the directions of maximum variance in geotechnical datasets, often corresponding to physically meaningful soil property combinations.
2. Reducing dimensionality before modeling can improve performance and interpretability when many correlated parameters are available.
3. The scree plot (explained variance vs. components) guides the choice of how many principal components to retain.

## Code Summary

- Applied PCA to a multi-parameter geotechnical dataset, projected high-dimensional soil data into 2D to reveal clustering, and compared PCA and t-SNE projections

## Geotechnical Application

- Reducing redundancy in large site investigation datasets with many correlated parameters and visualizing natural groupings in soil data

## Resources

- [Scikit-Learn PCA Documentation](https://scikit-learn.org/stable/modules/decomposition.html#pca)
- [StatQuest — PCA Explained](https://www.youtube.com/watch?v=FgakZw6K1QQ)

---

> *Day 034 of 100 — 100 Days of ML for Geotechnical Engineering*
