# Day 012: Modules & Packages

## Phase: Python Fundamentals

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- What a module is — any `.py` file that can be imported and reused
- The `import`, `from ... import`, and `import ... as` syntax variations
- Standard library modules useful for geotechnical work (`math`, `os`, `csv`, `json`, `datetime`, `statistics`, `pathlib`)
- Creating a custom `geotech_utils` module with reusable functions (SPT correction, bearing capacity, soil classification)
- The `if __name__ == "__main__"` guard — running a module as a script vs importing it as a library
- Organizing code into packages (directories with `__init__.py`)
- The module search path (`sys.path`) and how Python finds imports

## Key Takeaways

1. **Modules turn scripts into reusable libraries.** The soil classification functions, SPT correlations, and bearing capacity formulas from earlier days can live in a `geotech_utils.py` module and be imported into any future project with a single line.
2. **`if __name__ == "__main__"` separates reuse from testing.** Code inside this guard runs only when the file is executed directly, not when imported. This lets you keep test examples in the same file without polluting the importer's namespace.
3. **Standard library modules replace manual implementations.** `math.radians()`, `statistics.mean()`, `pathlib.Path()`, and `csv.DictReader` are battle-tested — using them instead of writing your own saves time and avoids bugs.

## Code Summary

- Explored key standard library modules: `math` for trigonometric functions in slope stability, `os` and `pathlib` for file path handling, `csv` and `json` for data interchange, `datetime` for timestamping field logs, `statistics` for quick descriptive stats on N-values
- Created a `geotech_utils.py` module containing: `correct_n60()` for energy-corrected SPT blow count, `estimate_bearing_capacity()` using Terzaghi's equation, `classify_soil_consistency()` based on SPT N-value ranges, and `compute_effective_stress()`
- Demonstrated importing the custom module with all three import styles
- Used the `__name__ == "__main__"` guard to include self-tests that only run when the module is executed directly

## Geotechnical Application

- **Reusable engineering functions:** SPT corrections, bearing capacity estimation, and soil classification packaged as importable utilities — write once, use across every project
- **Standard library for field data:** `csv` for borehole logs, `json` for lab test results, `datetime` for timestamped field observations, `pathlib` for cross-platform file management
- **Package structure for larger projects:** a `geotechnical/` package could contain sub-modules for `spt.py`, `cpt.py`, `classification.py`, and `plotting.py` — mirroring how real engineering software is organized

## Resources

- [Python Official Tutorial — Modules](https://docs.python.org/3/tutorial/modules.html)
- [Python Standard Library Reference](https://docs.python.org/3/library/index.html)
- [Real Python — Python Modules and Packages](https://realpython.com/python-modules-packages/)

---

> *Day 012 of 100 — 100 Days of ML for Geotechnical Engineering*
