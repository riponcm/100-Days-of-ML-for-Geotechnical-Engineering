# Day 075: Variational Autoencoders (VAE)

## Phase: Deep Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- VAE architecture: probabilistic encoder and decoder
- Latent space and the reparameterization trick
- ELBO loss: reconstruction loss + KL divergence
- Generating new samples from the learned latent space
- Comparing VAE with standard autoencoders

## Key Takeaways

1. VAEs learn a structured latent space that enables generating new, realistic data samples for data augmentation.
2. The KL divergence term regularizes the latent space, ensuring smooth interpolation between encoded samples.
3. VAE-generated synthetic samples can augment small geotechnical datasets, improving downstream model training.

## Code Summary

- Built a VAE for geotechnical data, visualized the latent space, and generated synthetic soil property profiles for data augmentation

## Geotechnical Application

- Generating synthetic geotechnical data to augment limited datasets and learning meaningful latent representations of soil behavior

## Resources

- [VAE Tutorial — PyTorch](https://pytorch.org/examples/vae/)
- [Auto-Encoding Variational Bayes (Kingma & Welling)](https://arxiv.org/abs/1312.6114)

---

> *Day 075 of 100 — 100 Days of ML for Geotechnical Engineering*
