# Day 074: Autoencoders

## Phase: Deep Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Autoencoder architecture: encoder, bottleneck, decoder
- Undercomplete autoencoders for dimensionality reduction
- Reconstruction loss and training procedure
- Denoising autoencoders for robust feature learning
- Anomaly detection using reconstruction error

## Key Takeaways

1. Autoencoders learn compressed representations of input data, useful for dimensionality reduction beyond what PCA offers.
2. Denoising autoencoders learn robust features by reconstructing clean data from corrupted inputs.
3. Anomaly detection with autoencoders identifies unusual samples by flagging high reconstruction errors.

## Code Summary

- Built autoencoders for geotechnical data compression and reconstruction, implemented a denoising variant, and applied anomaly detection based on reconstruction error

## Geotechnical Application

- Detecting anomalous soil test results, compressing high-dimensional geotechnical data, and denoising sensor measurements

## Resources

- [Autoencoder Tutorial — PyTorch](https://pytorch.org/tutorials/)
- [Introduction to Autoencoders — Keras](https://blog.keras.io/building-autoencoders-in-keras.html)

---

> *Day 074 of 100 — 100 Days of ML for Geotechnical Engineering*
