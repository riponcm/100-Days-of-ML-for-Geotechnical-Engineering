# Day 065: Activation Functions Deep Dive

## Phase: Deep Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- ReLU, Leaky ReLU, ELU, and GELU activations
- Sigmoid and Tanh for bounded outputs
- Dying ReLU problem and mitigation strategies
- Softmax for multi-class output layers
- Choosing activation functions for different layer positions

## Key Takeaways

1. ReLU is the default hidden layer activation due to its simplicity and effectiveness at preventing vanishing gradients.
2. The choice of output activation depends on the task: sigmoid for binary, softmax for multi-class, linear for regression.
3. Understanding activation properties helps diagnose training issues like dead neurons or saturated gradients.

## Code Summary

- Compared activation functions on a soil classification task, visualized their effects on gradient flow, and demonstrated the dying ReLU problem

## Geotechnical Application

- Selecting appropriate activation functions for neural networks predicting geotechnical properties or classifying soil conditions

## Resources

- [Activation Functions — ML Glossary](https://ml-cheatsheet.readthedocs.io/en/latest/activation_functions.html)
- [Deep Learning Book — Chapter 6](https://www.deeplearningbook.org/)

---

> *Day 065 of 100 — 100 Days of ML for Geotechnical Engineering*
