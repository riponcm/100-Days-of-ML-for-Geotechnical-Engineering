# Day 032: Data Preprocessing Pipeline

## Phase: Data Science Essentials

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- End-to-end preprocessing pipelines with Scikit-Learn Pipeline
- Column transformers for handling mixed data types
- Imputation strategies within pipelines
- Custom transformers using FunctionTransformer and TransformerMixin
- Preventing data leakage with proper train/test preprocessing

## Key Takeaways

1. Pipelines ensure that all preprocessing steps are applied consistently to training and test data, preventing data leakage.
2. Column transformers handle numerical and categorical columns with different strategies in a single, reproducible workflow.
3. Custom transformers allow incorporating domain-specific geotechnical transformations into the pipeline.

## Code Summary

- Built an end-to-end pipeline with imputation, scaling, encoding, and feature engineering, and created a custom transformer for geotechnical-specific preprocessing

## Geotechnical Application

- Building reproducible data processing workflows that consistently transform raw site investigation data into model-ready features

## Resources

- [Scikit-Learn Pipelines](https://scikit-learn.org/stable/modules/compose.html)
- [Scikit-Learn Column Transformer](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html)

---

> *Day 032 of 100 — 100 Days of ML for Geotechnical Engineering*
