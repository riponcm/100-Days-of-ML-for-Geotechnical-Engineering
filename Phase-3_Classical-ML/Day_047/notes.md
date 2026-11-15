# Day 047: DBSCAN & Hierarchical Clustering

## Phase: Classical Machine Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- DBSCAN: density-based clustering without specifying K
- Core points, border points, and noise detection
- Hierarchical (agglomerative) clustering and dendrograms
- Linkage methods: single, complete, average, Ward
- Comparing clustering algorithms on different data shapes

## Key Takeaways

1. DBSCAN automatically identifies the number of clusters and labels outliers as noise, useful for detecting anomalous soil samples.
2. Hierarchical clustering produces dendrograms that reveal the natural hierarchy of soil groupings at different similarity levels.
3. Different clustering algorithms suit different data structures: DBSCAN for irregular shapes, hierarchical for nested relationships.

## Code Summary

- Applied DBSCAN to detect soil anomalies, built dendrograms for hierarchical soil classification, and compared clustering approaches on geotechnical datasets

## Geotechnical Application

- Identifying outlier soil samples, discovering natural stratigraphic groupings, and detecting unusual test results in site investigation data

## Resources

- [Scikit-Learn DBSCAN](https://scikit-learn.org/stable/modules/clustering.html#dbscan)
- [Scikit-Learn Hierarchical Clustering](https://scikit-learn.org/stable/modules/clustering.html#hierarchical-clustering)

---

> *Day 047 of 100 — 100 Days of ML for Geotechnical Engineering*
