# Day 018: NumPy — Signal Processing Basics

## Phase: Data Science Essentials

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Discrete Fourier Transform (DFT) with np.fft
- Frequency domain representation of time-series signals
- Windowing functions and spectral leakage
- Convolution and correlation operations
- Sampling theorem and Nyquist frequency

## Key Takeaways

1. The FFT converts time-domain signals into frequency components, essential for analyzing seismic and vibration data.
2. Proper windowing reduces spectral leakage and improves frequency resolution in real-world measurements.
3. Convolution operations enable smoothing and filtering of noisy geotechnical sensor data directly in NumPy.

## Code Summary

- Applied FFT to a synthetic seismic acceleration time history, demonstrated windowing effects on spectral analysis, and used convolution for moving-average smoothing

## Geotechnical Application

- Frequency analysis of ground motion records and vibration monitoring data from construction sites or earthquake recordings

## Resources

- [NumPy FFT Documentation](https://numpy.org/doc/stable/reference/routines.fft.html)
- [Signal Processing Basics — SciPy Lecture Notes](https://scipy-lectures.org/)

---

> *Day 018 of 100 — 100 Days of ML for Geotechnical Engineering*
