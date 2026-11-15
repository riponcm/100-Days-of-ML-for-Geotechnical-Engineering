# Day 073: Time Series Forecasting with LSTM

## Phase: Deep Learning

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Sliding window approach for time series to supervised learning conversion
- Multi-step ahead forecasting strategies
- Sequence-to-sequence models for time series
- Handling trends, seasonality, and non-stationarity
- Evaluation metrics for time series forecasting

## Key Takeaways

1. The sliding window approach converts raw time series into input-output pairs suitable for LSTM training.
2. Multi-step forecasting accumulates errors, requiring careful model design and uncertainty quantification.
3. Proper time series splitting (chronological, no shuffling) prevents data leakage from future observations.

## Code Summary

- Built an LSTM time series forecaster for ground settlement data, implemented multi-step prediction, and evaluated forecast accuracy over different horizons

## Geotechnical Application

- Forecasting geotechnical time series: ground settlement during construction, pore pressure dissipation, and real-time monitoring predictions

## Resources

- [Time Series Forecasting with PyTorch](https://pytorch.org/tutorials/)
- [Forecasting Principles and Practice (Hyndman)](https://otexts.com/fpp3/)

---

> *Day 073 of 100 — 100 Days of ML for Geotechnical Engineering*
