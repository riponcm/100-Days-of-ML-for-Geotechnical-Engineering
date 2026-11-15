# Day 081: Tabular Deep Learning (TabNet)

## Phase: Deep Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Challenges of deep learning on tabular data vs. tree methods
- TabNet architecture: sequential attention and feature selection
- Sparse feature selection and interpretability in TabNet
- Self-supervised pre-training for tabular data
- Comparing TabNet with XGBoost and standard neural networks

## Key Takeaways

1. TabNet combines the interpretability of feature selection with the representation power of neural networks.
2. Attention-based feature selection in TabNet reveals which input features the model focuses on for each prediction.
3. For tabular geotechnical data, TabNet offers a deep learning alternative that can compete with gradient boosting methods.

## Code Summary

- Trained TabNet on a tabular geotechnical dataset, analyzed feature attention masks, and compared performance with XGBoost and standard MLPs

## Geotechnical Application

- Applying deep learning to tabular geotechnical datasets (soil properties, test results) where tree-based methods traditionally dominate

## Resources

- [TabNet Paper — Arik & Pfister](https://arxiv.org/abs/1908.07442)
- [pytorch-tabnet Library](https://github.com/dreamquark-ai/tabnet)

---

> *Day 081 of 100 — 100 Days of ML for Geotechnical Engineering*
