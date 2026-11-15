# Day 090: Seismic Response Spectra Prediction

## Phase: Geotechnical AI Capstone Projects

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Response spectra concepts and engineering significance
- Site amplification factors and site classification
- Neural network for spectral acceleration prediction at multiple periods
- Multi-output regression for simultaneous period predictions
- Comparison with code-based site factors (NEHRP, Eurocode)

## Key Takeaways

1. Multi-output neural networks can predict response spectra across all periods simultaneously, ensuring spectral shape consistency.
2. Site-specific ML predictions can capture local amplification effects that simplified code-based factors may miss.
3. Validating against recorded response spectra from instrumented sites ensures the model captures real site effects.

## Code Summary

- Built a multi-output neural network for response spectra prediction, compared with NEHRP site factors, and validated on recorded data

## Geotechnical Application

- Predicting site-specific response spectra for seismic design of structures on various soil conditions

## Resources

- [NEHRP Site Classification](https://www.usgs.gov/)
- [Ground Motion Models for Response Spectra](https://peer.berkeley.edu/)

---

> *Day 090 of 100 — 100 Days of ML for Geotechnical Engineering*
