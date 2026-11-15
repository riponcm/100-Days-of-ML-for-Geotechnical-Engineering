# Day 088: Soil Classification from CPT using CNN

## Phase: Geotechnical AI Capstone Projects

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- CPT data as 1D signal profiles for CNN input
- Designing 1D CNNs for soil layer classification
- Multi-channel input: qt, fs, u2 as parallel signals
- Sliding window classification for continuous profiling
- Comparison with Robertson chart-based classification

## Key Takeaways

1. 1D CNNs can learn spatial patterns in CPT profiles that correspond to soil behavior type transitions.
2. Multi-channel inputs allow the CNN to jointly process all CPT measurements for more accurate classification.
3. CNN-based classification achieves higher accuracy than chart-based methods by learning complex nonlinear patterns.

## Code Summary

- Built a 1D CNN for soil classification from CPT profiles, processed multi-channel inputs, and compared accuracy with Robertson classification

## Geotechnical Application

- Automating soil classification from Cone Penetration Test data for faster and more consistent stratigraphic profiling

## Resources

- [Robertson (2016) — CPT-based Soil Behavior Type](https://doi.org/10.1139/cgj-2016-0044)
- [Deep Learning for CPT Interpretation](https://www.sciencedirect.com/)

---

> *Day 088 of 100 — 100 Days of ML for Geotechnical Engineering*
