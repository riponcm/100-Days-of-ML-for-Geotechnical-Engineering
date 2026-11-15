# Day 063: PyTorch — Autograd & Backpropagation

## Phase: Deep Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Automatic differentiation with PyTorch autograd
- Computational graphs and gradient tracking
- Backpropagation through the graph with .backward()
- Gradient accumulation and zeroing
- Detaching tensors and no_grad context

## Key Takeaways

1. Autograd automatically computes gradients, eliminating the need to manually derive and code backpropagation equations.
2. Understanding gradient flow through computational graphs helps diagnose training issues like vanishing gradients.
3. Proper gradient management (zeroing, accumulation, detaching) is critical for correct training loops.

## Code Summary

- Demonstrated autograd on simple functions, traced computational graphs, and implemented a manual training loop using autograd-computed gradients

## Geotechnical Application

- Leveraging automatic differentiation for training neural networks on geotechnical data without manual gradient derivation

## Resources

- [PyTorch Autograd Tutorial](https://pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)
- [Automatic Differentiation — PyTorch](https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html)

---

> *Day 063 of 100 — 100 Days of ML for Geotechnical Engineering*
