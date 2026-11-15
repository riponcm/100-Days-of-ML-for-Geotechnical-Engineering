# Day 020: Pandas — Data Cleaning & Missing Values

## Phase: Data Science Essentials

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Identifying missing data with .isnull(), .isna(), and .info()
- Strategies for handling missing values: drop, fill, interpolate
- Detecting and removing duplicate records
- Data type conversion and fixing inconsistent entries
- Outlier detection using IQR and z-score methods

## Key Takeaways

1. Missing data is extremely common in geotechnical datasets due to incomplete sampling and test failures, making cleaning skills essential.
2. Interpolation methods (linear, depth-weighted) are often more appropriate than simple mean imputation for spatially correlated soil data.
3. Systematic data cleaning should precede any analysis to avoid biased or erroneous model results.

## Code Summary

- Loaded a messy borehole dataset with missing values, duplicates, and type errors, applied multiple imputation strategies, and built a reusable cleaning function

## Geotechnical Application

- Cleaning real-world site investigation data where SPT refusal, lost samples, and incomplete lab results create gaps in the dataset

## Resources

- [Pandas — Working with Missing Data](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Data Cleaning with Python and Pandas](https://realpython.com/python-data-cleaning-numpy-pandas/)

---

> *Day 020 of 100 — 100 Days of ML for Geotechnical Engineering*
