# Day 028: SciPy — Interpolation & Curve Fitting

## Phase: Data Science Essentials

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- 1D interpolation: linear, cubic, and spline methods
- scipy.interpolate.interp1d and CubicSpline
- Curve fitting with scipy.optimize.curve_fit
- 2D interpolation and gridding with griddata
- Choosing appropriate fitting models for geotechnical data

## Key Takeaways

1. Interpolation fills gaps between discrete measurement depths, creating continuous soil property profiles from sparse borehole data.
2. Curve fitting enables deriving empirical correlations (e.g., SPT-N vs. shear wave velocity) by fitting parametric models to field data.
3. 2D interpolation is critical for generating spatial contour maps of soil properties across a site from scattered borehole locations.

## Code Summary

- Interpolated SPT-N values between measurement depths using cubic splines, fitted power-law correlations to SPT-N vs. Vs data, and created 2D contour maps

## Geotechnical Application

- Generating continuous soil profiles from discrete test data and developing site-specific empirical correlations between geotechnical parameters

## Resources

- [SciPy Interpolation Documentation](https://docs.scipy.org/doc/scipy/reference/interpolate.html)
- [SciPy curve_fit Tutorial](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)

---

> *Day 028 of 100 — 100 Days of ML for Geotechnical Engineering*
