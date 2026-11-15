# Day 067: Regularization (Dropout, BatchNorm)

## Phase: Deep Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Dropout: randomly deactivating neurons during training
- Batch Normalization: normalizing layer inputs
- L2 regularization (weight decay) in deep learning
- Data augmentation as implicit regularization
- Early stopping as a regularization strategy

## Key Takeaways

1. Dropout prevents co-adaptation of neurons, improving generalization especially on small geotechnical datasets.
2. Batch normalization stabilizes training by reducing internal covariate shift, enabling higher learning rates.
3. Combining multiple regularization techniques (dropout + weight decay + early stopping) often yields the best results.

## Code Summary

- Applied dropout, batch normalization, and weight decay to a neural network, compared training dynamics, and demonstrated improved generalization

## Geotechnical Application

- Preventing overfitting when training deep learning models on limited geotechnical datasets with many parameters

## Resources

- [Dropout Paper — Srivastava et al.](https://jmlr.org/papers/v15/srivastava14a.html)
- [Batch Normalization Paper — Ioffe & Szegedy](https://arxiv.org/abs/1502.03167)

---

> *Day 067 of 100 — 100 Days of ML for Geotechnical Engineering*
