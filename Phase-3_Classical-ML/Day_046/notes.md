# Day 046: K-Means Clustering

## Phase: Classical Machine Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- K-Means algorithm: initialization, assignment, update steps
- Choosing K with the elbow method and silhouette score
- K-Means++ initialization for better convergence
- Limitations: sensitivity to scale, shape, and outliers
- Cluster interpretation and labeling

## Key Takeaways

1. K-Means can discover natural soil groupings in site investigation data without predefined classification labels.
2. The elbow method and silhouette scores help determine the optimal number of soil clusters in a dataset.
3. Feature scaling is essential before clustering to prevent parameters with larger scales from dominating cluster assignments.

## Code Summary

- Applied K-Means to cluster soil samples by index properties, used the elbow method to select K, and interpreted clusters as soil types

## Geotechnical Application

- Automated grouping of soil samples into distinct types based on measured properties when formal classification labels are unavailable

## Resources

- [Scikit-Learn K-Means](https://scikit-learn.org/stable/modules/clustering.html#k-means)
- [K-Means Clustering Visualization](https://www.naftaliharris.com/blog/visualizing-k-means-clustering/)

---

> *Day 046 of 100 — 100 Days of ML for Geotechnical Engineering*
