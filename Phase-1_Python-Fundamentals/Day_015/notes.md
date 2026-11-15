# Day 015: Mini Project — USCS Soil Classification Tool

## Phase: Python Fundamentals

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- The Unified Soil Classification System (USCS) per ASTM D2487 — classifying soils by grain size distribution and Atterberg limits
- Integrating all Phase 1 Python concepts into a single working application
- Designing classes to represent soil samples with their index properties
- Using conditionals for the multi-branch USCS decision tree (coarse-grained vs fine-grained, gravel vs sand, high vs low plasticity)
- Reading soil sample data from CSV, processing each sample, and writing classified results
- Error handling for invalid or missing lab data
- Functions for computing derived properties: plasticity index (PI = LL - PL), percent passing specific sieves, coarse-to-fine ratio

## Key Takeaways

1. **The USCS decision tree is a natural fit for Python conditionals and OOP.** The classification starts with percent passing the No. 200 sieve (fine-grained vs coarse-grained), then branches on the No. 4 sieve (gravel vs sand), then on Atterberg limits and gradation — each branch maps directly to `if/elif` logic inside a `classify()` method.
2. **This project uses every Phase 1 skill.** Variables and types store soil properties. Conditionals implement the classification logic. Loops process multiple samples. Dictionaries map USCS symbols to descriptions. Functions and classes organize the code. File I/O reads input and writes results. Error handling skips bad rows gracefully.
3. **Soil classification is the foundation of geotechnical ML.** Before any model can predict bearing capacity, liquefaction potential, or settlement, the soil must be classified. Automating USCS classification with Python is the first step toward building training datasets with consistent, reproducible labels.

## Code Summary

- Built a `SoilSample` class with attributes: `sample_id`, `depth`, `percent_gravel`, `percent_sand`, `percent_fines`, `liquid_limit`, `plastic_limit`, `Cu` (coefficient of uniformity), `Cc` (coefficient of curvature)
- Implemented `classify()` method following the full USCS decision tree:
  - Coarse-grained (fines < 50%): Gravel (G) vs Sand (S), then Well-graded (W) vs Poorly-graded (P) based on Cu and Cc, with dual symbols (e.g., SW-SM) when fines are 5-12%
  - Fine-grained (fines >= 50%): Clay (C) vs Silt (M) based on plasticity chart position, then High (H) vs Low (L) plasticity based on LL = 50 boundary
- Read soil samples from `soil_samples.csv` using `csv.DictReader`
- Applied the classifier to each sample with error handling for missing or invalid data
- Output classified results as a formatted report and CSV

## Geotechnical Application

- **USCS classification** is the most widely used soil classification system in geotechnical practice (ASTM D2487) — every foundation design, slope stability analysis, and earthwork specification starts with it
- **Automating classification** eliminates manual lookup errors and ensures consistency across large datasets — critical when processing hundreds of lab test results from a major project
- **The classified output becomes training data** for ML models — soil class labels (GW, SP, CL, CH, ML, etc.) serve as categorical features or target variables in prediction tasks

## Resources

- ASTM D2487 — Standard Practice for Classification of Soils (Unified Soil Classification System)
- Das, B.M. — Principles of Geotechnical Engineering (USCS classification chapter)
- [USDA NRCS — Unified Soil Classification System Guide](https://www.nrcs.usda.gov/)

---

> *Day 015 of 100 — 100 Days of ML for Geotechnical Engineering*
