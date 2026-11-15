# Day 085: Ground Motion Prediction with LSTM

## Phase: Deep Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Ground motion time series characteristics
- LSTM-based sequence-to-sequence prediction for ground motion
- Input feature engineering: site conditions, source parameters
- Peak ground acceleration (PGA) and spectral acceleration prediction
- Comparison with Ground Motion Prediction Equations (GMPEs)

## Key Takeaways

1. LSTMs can capture temporal patterns in ground motion records that traditional attenuation relationships miss.
2. Combining site-specific features with sequence modeling enables site-dependent ground motion predictions.
3. LSTM predictions should be benchmarked against established GMPEs to validate their accuracy and reliability.

## Code Summary

- Trained an LSTM to predict ground motion parameters, compared with NGA-West2 GMPEs, and analyzed prediction uncertainty

## Geotechnical Application

- Predicting site-specific ground motion characteristics for seismic design of geotechnical structures and earthquake hazard assessment

## Resources

- [NGA-West2 Ground Motion Models](https://peer.berkeley.edu/research/nga-west-2)
- [Deep Learning for Ground Motion — Recent Studies](https://www.sciencedirect.com/)

---

> *Day 085 of 100 — 100 Days of ML for Geotechnical Engineering*
