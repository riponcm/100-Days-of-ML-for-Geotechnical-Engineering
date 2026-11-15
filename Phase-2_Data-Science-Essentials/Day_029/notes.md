# Day 029: SciPy — Signal Processing (FFT, Filtering)

## Phase: Data Science Essentials

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Fast Fourier Transform (FFT) with scipy.fft
- Designing and applying digital filters (Butterworth, Chebyshev)
- Low-pass, high-pass, and band-pass filtering
- Spectrogram and Short-Time Fourier Transform (STFT)
- Response spectra computation from acceleration time histories

## Key Takeaways

1. Band-pass filtering isolates frequency ranges of interest in seismic records, removing instrument noise and baseline drift.
2. Spectrograms reveal how frequency content evolves over time during an earthquake, useful for site response analysis.
3. SciPy's signal module provides a complete toolkit for processing ground motion records used in geotechnical earthquake engineering.

## Code Summary

- Computed FFT of earthquake acceleration records, applied Butterworth band-pass filters to clean raw seismic data, and generated spectrograms

## Geotechnical Application

- Processing strong motion records for site response analysis, filtering seismic signals, and computing response spectra for foundation design

## Resources

- [SciPy Signal Processing Documentation](https://docs.scipy.org/doc/scipy/reference/signal.html)
- [Earthquake Signal Processing Basics](https://www.seismosignal.com/)

---

> *Day 029 of 100 — 100 Days of ML for Geotechnical Engineering*
