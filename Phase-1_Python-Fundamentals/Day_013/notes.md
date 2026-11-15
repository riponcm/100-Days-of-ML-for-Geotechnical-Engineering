# Day 013: Decorators & Generators

## Phase: Python Fundamentals

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Functions as first-class objects — passing functions as arguments and returning them
- Closures — inner functions that remember the enclosing scope
- Decorators — wrapping a function to add behavior without modifying it (`@decorator` syntax)
- Writing a `@timer` decorator to measure function execution time
- Writing a `@validate_input` decorator to check engineering constraints before computation
- Generator functions using `yield` — producing values lazily one at a time instead of building an entire list in memory
- Generator expressions as memory-efficient alternatives to list comprehensions
- Chaining generators into data processing pipelines

## Key Takeaways

1. **Decorators add behavior without touching the original function.** A `@timer` decorator can measure how long any SPT correction or bearing capacity calculation takes. A `@validate_input` decorator can reject negative N-values or impossible depths before the function body even runs — separation of concerns in action.
2. **Generators handle large datasets without loading everything into memory.** When processing thousands of borehole readings from a large CSV, `yield` produces one row at a time. This is the same concept behind how Pandas reads files in chunks and how PyTorch `DataLoader` streams training batches.
3. **Both patterns are everywhere in ML frameworks.** Decorators appear as `@staticmethod`, `@property`, `@torch.no_grad()`. Generators power data pipelines, batch iteration, and streaming predictions.

## Code Summary

- Built a `@timer` decorator that logs execution time for any geotechnical computation
- Built a `@validate_input` decorator that checks whether SPT N-values and depths are within valid engineering ranges before processing
- Demonstrated stacking multiple decorators on a single function
- Built a `borehole_data_stream()` generator that reads borehole CSV data row-by-row using `yield`, suitable for files too large to fit in memory
- Built a generator pipeline: `read_rows()` -> `filter_valid()` -> `compute_n60()` -> `classify()`, each stage yielding to the next
- Compared memory usage of list-based vs generator-based approaches on a large synthetic dataset

## Geotechnical Application

- **`@timer` for performance monitoring:** measure how long liquefaction analysis or settlement calculations take on large datasets — essential when scaling to hundreds of boreholes
- **`@validate_input` for data quality:** automatically reject impossible field values (N60 < 0, depth < 0, unit weight outside physical range) before they corrupt downstream calculations
- **Generators for streaming field data:** process large site investigation databases (thousands of CPT soundings, continuous sampling logs) without loading everything into RAM
- **Pipeline pattern for ETL:** read raw field data, filter bad rows, apply corrections, classify — each step as a generator feeding the next, exactly like a scikit-learn `Pipeline`

## Resources

- [Python Official Tutorial — Decorators (PEP 318)](https://peps.python.org/pep-0318/)
- [Python Official Tutorial — Generators (PEP 255)](https://peps.python.org/pep-0255/)
- [Real Python — Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)

---

> *Day 013 of 100 — 100 Days of ML for Geotechnical Engineering*
