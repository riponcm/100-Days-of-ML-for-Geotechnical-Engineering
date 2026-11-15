# Day 084: Seismic Signal Classification (DL)

## Phase: Deep Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Seismic signal characteristics and classification objectives
- 1D CNN for waveform classification
- Spectrogram-based classification with 2D CNNs
- Data preprocessing for seismic signals (filtering, normalization)
- Model evaluation on seismic event classification

## Key Takeaways

1. 1D CNNs can directly process raw seismic waveforms, learning discriminative features without manual feature extraction.
2. Spectrogram representations enable 2D CNNs to leverage image classification capabilities for signal classification.
3. Proper signal preprocessing (baseline correction, filtering) is essential before training deep learning models on seismic data.

## Code Summary

- Built 1D and 2D CNN classifiers for seismic signal classification, compared performance on waveform vs. spectrogram inputs, and analyzed learned features

## Geotechnical Application

- Classifying seismic events (earthquake types, blast vs. earthquake, noise vs. signal) for geotechnical earthquake engineering applications

## Resources

- [Deep Learning for Seismology — Mousavi et al.](https://doi.org/10.1126/science.aaz7103)
- [ObsPy — Seismological Data Processing](https://docs.obspy.org/)

---

> *Day 084 of 100 — 100 Days of ML for Geotechnical Engineering*
