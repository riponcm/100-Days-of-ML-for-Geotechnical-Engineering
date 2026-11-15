# Day 070: Transfer Learning (ResNet, VGG)

## Phase: Deep Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Transfer learning concept: leveraging pre-trained models
- Fine-tuning vs. feature extraction strategies
- ResNet architecture and skip connections
- VGG architecture and depth
- Adapting pre-trained models to new domains

## Key Takeaways

1. Transfer learning allows achieving high accuracy on small geotechnical image datasets by leveraging features learned on ImageNet.
2. Fine-tuning deeper layers while freezing early layers is effective when the target domain differs from the pre-training domain.
3. ResNet's skip connections solve the vanishing gradient problem, enabling very deep architectures that improve feature extraction.

## Code Summary

- Applied transfer learning with ResNet and VGG to a geotechnical image classification task, compared fine-tuning strategies, and achieved high accuracy with limited data

## Geotechnical Application

- Using pre-trained deep learning models for geotechnical image analysis when labeled training data is scarce

## Resources

- [PyTorch Transfer Learning Tutorial](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html)
- [ResNet Paper — He et al.](https://arxiv.org/abs/1512.03385)

---

> *Day 070 of 100 — 100 Days of ML for Geotechnical Engineering*
