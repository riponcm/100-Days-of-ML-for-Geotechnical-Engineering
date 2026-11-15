# Phase 1: Python Fundamentals

**Days:** 001 -- 015  
**Goal:** Build a rock-solid Python foundation, with every concept grounded in geotechnical engineering context.

---

## Learning Progression

Phase 1 moves from zero Python knowledge to a fully functional engineering tool. The first week covers core language mechanics (variables, control flow, data structures, functions). The second week introduces software engineering concepts (file I/O, error handling, OOP, modules). The phase culminates in a mini project that integrates everything into a USCS Soil Classification Tool.

---

## Day-by-Day Overview

| Day | Topic | What You Build / Learn |
|-----|-------|----------------------|
| 001 | Variables, Data Types & Type Casting | Store soil properties (depth, N-value, unit weight) as Python variables; convert between types |
| 002 | Conditionals -- if / elif / else | Classify soil consistency from SPT N-values using branching logic |
| 003 | Loops -- for, while, enumerate, zip | Process multiple borehole layers in a loop; pair depths with N-values using zip |
| 004 | Strings & String Methods | Format borehole reports; parse and clean soil description text |
| 005 | Lists, Tuples & Sets | Store borehole data in ordered collections; use sets for unique soil types |
| 006 | Dictionaries & Comprehensions | Map borehole IDs to properties; build lookup tables with comprehensions |
| 007 | Functions & Lambda Expressions | Write reusable SPT correction functions; use lambda for quick inline calculations |
| 008 | File I/O -- Read & Write CSV, TXT | Read field CSV data, process it, write analysis results -- the complete field-to-report pipeline |
| 009 | Error Handling -- try / except / finally | Handle messy field data ("NR", blanks, wrong formats) without crashing; skip bad rows, keep good ones |
| 010 | OOP -- Classes & Objects | Build `SoilLayer` and `BoreholeLog` classes with methods for Vs estimation, consistency classification, and stress computation |
| 011 | OOP -- Inheritance & Polymorphism | Build `GeotechTest` base class with `SPTTest`, `CPTTest`, and `TriaxialTest` children; process mixed test data polymorphically |
| 012 | Modules & Packages | Use standard library modules; create a reusable `geotech_utils` module; understand `__name__ == "__main__"` |
| 013 | Decorators & Generators | Write `@timer` and `@validate_input` decorators; use `yield` to stream large borehole datasets without loading everything into memory |
| 014 | Regular Expressions | Parse unstructured borehole log text to extract N-values, depths, and soil descriptions using the `re` module |
| 015 | Mini Project -- USCS Soil Classification Tool | Integrate all Phase 1 concepts into a complete USCS classifier (ASTM D2487) that reads soil samples from CSV and outputs classified results |

---

## Skills Acquired

By the end of Phase 1, you can:

- Store, transform, and validate geotechnical data using Python's built-in types and structures
- Write clean, reusable functions and classes for engineering calculations
- Read and write field data files (CSV, TXT, JSON)
- Handle messy real-world data with error handling and regex
- Organize code into importable modules
- Build a working engineering tool from scratch

---

## Folder Structure

Each day folder contains:

- `day_XXX.ipynb` -- Jupyter Notebook (also uploaded to Kaggle)
- `notes.md` (or `readme.md` for earlier days) -- Key concepts and takeaways
- Additional data files where applicable (e.g., `soil_samples.csv` for Day 015)

---

## What Comes Next

Phase 2 (Data Science Essentials, Days 016--030) builds on this foundation with NumPy, Pandas, Matplotlib, and exploratory data analysis on real geotechnical datasets.

---

> *Part of [100 Days of ML for Geotechnical Engineering](../README.md)*
