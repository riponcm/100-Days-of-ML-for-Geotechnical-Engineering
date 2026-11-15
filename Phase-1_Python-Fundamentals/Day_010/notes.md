# Day 010: OOP — Classes & Objects

## Phase: Python Fundamentals

**Date:** February 25, 2026  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Classes as blueprints and objects as instances built from them
- The `__init__` constructor for setting up object attributes
- Instance methods that operate on an object's own data via `self`
- `__str__` and `__repr__` for human-readable and developer-readable output
- Class attributes (shared constants like `gravity = 9.81`) vs instance attributes (unique per object)
- Composition — objects containing other objects (a `BoreholeLog` holds a list of `SoilLayer` objects)

## Key Takeaways

1. **A class bundles data and behavior together.** Instead of tracking depth, N60, soil type, and unit weight in four parallel lists, a single `SoilLayer` object carries all its properties and can classify itself, estimate Vs, or compute overburden stress.
2. **`__init__` + `self` is the core pattern.** `self.depth = depth` saves data on the object so every method can access it without extra arguments. Every scikit-learn model uses this same pattern.
3. **Composition mirrors real engineering data.** A `BoreholeLog` object holds a list of `SoilLayer` objects, just like a real borehole report contains multiple soil layers — this is far cleaner than nested dictionaries or parallel arrays.

## Code Summary

- Built a `SoilLayer` class with `__init__`, `classify_consistency()`, `estimate_vs()` (Imai & Tonouchi 1982), `overburden_stress()`, `effective_stress()`, `estimate_friction_angle()`, and `is_cohesive()`
- Built a `BoreholeLog` class using composition — stores a list of `SoilLayer` objects and provides `add_layer()`, `find_weakest_layer()`, `find_strongest_layer()`, `average_N60()`, `layers_below_water_table()`, `check_liquefaction_risk()`, and `generate_report()`
- Demonstrated class attributes for shared physical constants (gravity, water density, atmospheric pressure)
- Compared OOP approach vs parallel-list approach to show the readability and safety advantage
- Created and compared two boreholes (BH-01 and BH-02) side by side

## Geotechnical Application

- **SoilLayer** models a single stratum from a borehole log with SPT-based consistency classification (Very Loose through Very Dense) and shear wave velocity estimation
- **BoreholeLog** models an entire borehole with multi-layer analysis, water table tracking, effective stress computation, and simplified liquefaction screening
- The composition pattern (`BoreholeLog` containing `SoilLayer` objects) directly mirrors how geotechnical data is structured in practice — one site has many boreholes, each borehole has many layers

## Resources

- [Python Official Tutorial — Classes](https://docs.python.org/3/tutorial/classes.html)
- Imai, T. & Tonouchi, K. (1982) — Correlation of N-value with S-wave velocity
- Peck, Hanson & Thornburn (1974) — SPT correlations for friction angle

---

> *Day 010 of 100 — 100 Days of ML for Geotechnical Engineering*
