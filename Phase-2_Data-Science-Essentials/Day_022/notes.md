# Day 022: Pandas — Merge, Join & Concat

## Phase: Data Science Essentials

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Concatenating DataFrames with pd.concat() along rows and columns
- Merge operations: inner, outer, left, right joins
- Merging on single and multiple keys
- Handling overlapping column names and suffixes
- Index-based joining with .join()

## Key Takeaways

1. Merging allows combining field test results with laboratory data using shared keys like borehole ID and depth.
2. Understanding join types prevents accidental data loss (inner join) or unintended null rows (outer join).
3. Concatenation is ideal for combining data from multiple boreholes or investigation campaigns into a unified dataset.

## Code Summary

- Merged SPT field data with lab test results on borehole ID and depth, concatenated data from multiple site investigation phases, and compared join types

## Geotechnical Application

- Integrating field testing data (SPT, CPT) with laboratory results (Atterberg limits, grain size) from different data sources into a unified site model

## Resources

- [Pandas — Merge, Join, Concatenate](https://pandas.pydata.org/docs/user_guide/merging.html)
- [Pandas Merging 101](https://stackoverflow.com/questions/53645882/pandas-merging-101)

---

> *Day 022 of 100 — 100 Days of ML for Geotechnical Engineering*
