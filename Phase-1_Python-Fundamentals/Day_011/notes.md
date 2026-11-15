# Day 011: OOP — Inheritance & Polymorphism

## Phase: Python Fundamentals

**Date:** February 27, 2026  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- Inheritance — child classes reusing attributes and methods from a parent class
- `super().__init__()` to call the parent constructor and avoid duplicating common fields
- Method overriding — child classes replacing parent methods with specialized logic
- Polymorphism — calling the same method name on objects of different types, each responding with its own behavior
- `isinstance()` vs `type()` for type checking that respects the inheritance chain
- Multiple inheritance and mixins (`Printable`, `Exportable`) for cross-cutting capabilities
- Method Resolution Order (MRO) — how Python resolves method calls in complex hierarchies

## Key Takeaways

1. **Inheritance eliminates duplicated code.** Common fields (`borehole_id`, `depth`, `date`) live in the `GeotechTest` base class. `SPTTest`, `CPTTest`, and `TriaxialTest` each inherit them via `super().__init__()` and add only what is unique.
2. **Polymorphism removes type-checking branches.** Instead of writing `if isinstance(test, SPTTest): ... elif isinstance(test, CPTTest): ...`, you call `test.classify()` in one loop and each class runs its own version automatically.
3. **This is exactly how scikit-learn works.** When you write `model.fit(X, y)`, you are using polymorphism — `RandomForest.fit()` and `SVM.fit()` both override a base `fit()` method. Understanding today's pattern unlocks reading ML library source code.

## Code Summary

- Built a `GeotechTest` base class with `summary()`, `analyze()`, and `classify()` placeholder methods
- Built `SPTTest` child class — stores N-value, computes N60 correction, estimates Vs, classifies relative density
- Built `CPTTest` child class — stores tip resistance and sleeve friction, computes friction ratio, classifies via simplified Robertson chart
- Built `TriaxialTest` child class — stores confining pressure, deviator stress, cohesion, and friction angle; computes Mohr-Coulomb shear strength
- Created `Printable` and `Exportable` mixins, combined them with `SPTTest` via multiple inheritance (`EnhancedSPT`)
- Built a complete site investigation report system — 14 mixed tests across 3 boreholes, processed polymorphically in a single loop with per-borehole and cross-site statistics

## Geotechnical Application

- **SPT analysis:** N60 energy correction, relative density classification (Very Loose to Very Dense), Vs estimation
- **CPT analysis:** friction ratio computation, simplified Robertson soil behavior type classification
- **Triaxial analysis:** Mohr-Coulomb shear strength (`tau = c + sigma_n * tan(phi)`), strength-based classification
- **Unified site report:** mixed test types from multiple boreholes processed through a single interface — mirrors how real geotechnical reporting software must handle heterogeneous field and lab data

## Resources

- [Python Official Tutorial — Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- Robertson, P.K. (1990) — Soil classification using the CPT
- ASTM D1586 — Standard Penetration Test
- ASTM D4767 — Consolidated Undrained Triaxial Compression Test

---

> *Day 011 of 100 — 100 Days of ML for Geotechnical Engineering*
