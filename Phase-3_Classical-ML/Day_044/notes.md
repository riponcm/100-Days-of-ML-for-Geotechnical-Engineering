# Day 044: Support Vector Machines (SVM)

## Phase: Classical Machine Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- SVM theory: maximum margin classifiers and support vectors
- Kernel trick: RBF, polynomial, and linear kernels
- Soft margin classification with the C parameter
- SVM for regression (SVR)
- Scaling requirements and computational considerations

## Key Takeaways

1. SVMs find the optimal separating hyperplane, making them effective for soil classification with well-separated classes.
2. The kernel trick enables SVMs to handle nonlinear decision boundaries without explicitly computing high-dimensional features.
3. SVM performance is highly sensitive to feature scaling and hyperparameter selection (C, gamma).

## Code Summary

- Trained SVM classifiers with different kernels for soil classification, visualized support vectors and margins, and applied SVR for continuous prediction

## Geotechnical Application

- Classifying soil types and predicting properties when the relationship between features and targets is complex and nonlinear

## Resources

- [Scikit-Learn SVM](https://scikit-learn.org/stable/modules/svm.html)
- [SVM Tutorial — MIT](https://web.mit.edu/6.034/wwwbob/svm-notes-long-08.pdf)

---

> *Day 044 of 100 — 100 Days of ML for Geotechnical Engineering*
