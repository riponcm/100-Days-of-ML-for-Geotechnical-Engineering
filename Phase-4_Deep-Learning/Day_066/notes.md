# Day 066: Loss Functions & Optimizers

## Phase: Deep Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Loss functions for regression: MSE, MAE, Huber loss
- Loss functions for classification: cross-entropy, focal loss
- Optimizers: SGD with momentum, Adam, AdamW, RMSProp
- Learning rate scheduling: step, cosine, warm-up
- Impact of optimizer choice on convergence behavior

## Key Takeaways

1. Huber loss combines the best of MSE and MAE, being robust to outliers while maintaining smooth gradients near zero.
2. Adam optimizer adapts learning rates per parameter, generally converging faster than vanilla SGD on most problems.
3. Learning rate scheduling can significantly improve final model performance by allowing fine-tuning in later training stages.

## Code Summary

- Compared loss functions and optimizers on a geotechnical regression task, visualized convergence curves, and demonstrated learning rate scheduling

## Geotechnical Application

- Choosing appropriate loss functions and optimizers for neural networks trained on geotechnical data with varying noise levels and outliers

## Resources

- [PyTorch Loss Functions](https://pytorch.org/docs/stable/nn.html#loss-functions)
- [PyTorch Optimizers](https://pytorch.org/docs/stable/optim.html)

---

> *Day 066 of 100 — 100 Days of ML for Geotechnical Engineering*
