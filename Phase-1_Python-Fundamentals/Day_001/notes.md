# Day 001 | Variables, Data Types & Type Casting

**100 Days of ML for Geotechnical Engineering**
Phase 1: Python Fundamentals
Author: Ripon Chandra Malo
Date: February 16, 2026

---

## Geotechnical Problem We Solved Today

We received field data from an **SPT (Standard Penetration Test) borehole investigation** for a highway bridge foundation in Salt Lake City. The field crew sent everything as text from a digital tablet form. Our job was to:

1. Store the data properly in Python (variables)
2. Understand what kind of data each piece is (data types)
3. Convert text to numbers for calculations (type casting)
4. Perform basic SPT correlations (real engineering application)

This is the exact first step before any ML model — **clean your data.**

---

## Concept 1: Variables

A variable is a **labeled container** that holds data. Like a jar in your kitchen — the label tells you what's inside, and you can change the contents anytime.

```python
borehole_depth = 15.5          # a jar labeled "borehole_depth" holding 15.5
spt_n_value = 18               # a jar labeled "spt_n_value" holding 18
soil_type = "Silty Sand"       # a jar labeled "soil_type" holding text
is_saturated = False           # a jar labeled "is_saturated" holding False
```

### Naming Rules

| Rule | Good Example | Bad Example | Why |
|------|-------------|-------------|-----|
| Start with letter or _ | `depth`, `_temp` | `1st_layer` | Can't start with number |
| No spaces | `water_table_depth` | `water table depth` | Use underscores |
| Be descriptive | `spt_n_value` | `x` | You (and your ML model) need clarity |
| Case sensitive | `Depth` ≠ `depth` | — | Be consistent, use lowercase |

### Geotechnical Application

Every borehole log has these variables: project name, borehole ID, depth, water table, N-values, soil descriptions. In Python, each becomes a variable. Later (Phase 2), these become columns in a Pandas DataFrame.

---

## Concept 2: Data Types

Python has **4 basic types** we use constantly:

| Type | Python Name | Example | Geotechnical Use |
|------|------------|---------|------------------|
| Integer | `int` | `18` | SPT N-value, number of layers, blow count |
| Float | `float` | `15.5` | Depth, unit weight, pressure, Vs |
| String | `str` | `"Silty Sand"` | Soil name, borehole ID, project name |
| Boolean | `bool` | `True`/`False` | Saturated? Liquefiable? Stable? |

### How to check a type

```python
type(borehole_depth)      # → <class 'float'>
type(spt_n_value)         # → <class 'int'>
type(soil_type)           # → <class 'str'>
type(is_saturated)        # → <class 'bool'>
```

### Why does this matter?

- **Numbers** (int, float) → used for math, plots, ML model training
- **Text** (str) → must be encoded/converted before ML can use it
- **Boolean** (bool) → used for filtering data, labeling, classification

Wrong types = bugs in your code. Correct types = smooth data pipeline.

### Mixing types

- `int + float` → works (Python auto-converts int to float)
- `str + str` → works (joins them: `"BH" + "-01"` → `"BH-01"`)
- `str + int` → **ERROR!** Must convert first with `str()`

---

## Concept 3: Type Casting

Type casting means **converting data from one type to another**. You do this with four functions:

| Function | What It Does | Example |
|----------|-------------|---------|
| `int()` | Convert to integer | `int("24")` → `24` |
| `float()` | Convert to float | `float("6.5")` → `6.5` |
| `str()` | Convert to string | `str(18)` → `"18"` |
| `bool()` | Convert to boolean | `bool(0)` → `False` |

### Real Scenarios in Geotechnical Work

**Scenario 1: Field data arrives as text**

Every digital form, CSV file, and GPS logger sends data as strings. You must convert before calculating.

```python
field_n_value = "24"              # String from tablet form
N = int(field_n_value)            # Now it's 24 (integer)

field_depth = "6.5"               # String from GPS
depth = float(field_depth)        # Now it's 6.5 (float)
```

**Scenario 2: Building report labels**

```python
layer_number = 3
depth_value = 4.5
label = f"Layer-{layer_number} at {depth_value}m"
# Result: "Layer-3 at 4.5m"
```

Use **f-strings** (the `f"..."` syntax). They are the modern, clean way to mix text and numbers.

**Scenario 3: Boolean / Truthiness**

```python
bool(0)       # → False   (N=0 means no resistance — very soft!)
bool(15)      # → True    (N=15 means soil has strength)
bool("")      # → False   (empty string — no data)
bool("Clay")  # → True    (has data)
```

This becomes critical when filtering datasets in Phase 2-3.

**Scenario 4: Float vs Integer precision**

```python
int(22.7)     # → 22   (TRUNCATES — cuts off decimal, no rounding!)
round(22.7)   # → 23   (ROUNDS — mathematically correct)
round(18.567, 2)  # → 18.57   (round to 2 decimal places)
```

Use `round()` for engineering calculations. Use `int()` only when you intentionally want to truncate.

---

## Complete Geotechnical Workflow

This is what we built in the notebook — the full pipeline:

```
Raw Field Data    →    Type Casting    →    Calculations    →    Report
(all strings)         (int, float)        (N60, Vs, σv)       (formatted output)
```

### Step-by-step

1. **Receive raw data** — all strings from field form
2. **Cast types** — `int()` for N-values, `float()` for depths
3. **Calculate N60** — `N60 = N × (Ce / 0.60)` (energy correction)
4. **Estimate Vs** — `Vs = 97 × N60^0.314` (Imai & Tonouchi, 1982)
5. **Check saturation** — `is_saturated = depth > water_table_depth` (boolean)
6. **Classify soil** — if/elif chain based on N60 range
7. **Generate report** — f-strings to format output

### Key Formulas Used

| Formula | Meaning |
|---------|---------|
| `N60 = N × (Ce / 0.60)` | Correct raw SPT N for hammer efficiency |
| `σv = γ × depth` | Overburden pressure at sample depth |
| `Vs = 97 × N60^0.314` | Shear wave velocity from SPT (Imai & Tonouchi) |
| `Dr = 21 × √N60` | Relative density for sands (Meyerhof) |

---

## How This Connects to ML (Preview)

| What We Did Today | What It Becomes in ML (Phase 2-5) |
|-------------------|------------------------------------|
| Store data in variables | Store in NumPy arrays and Pandas DataFrames |
| Check data types | Data validation in preprocessing pipelines |
| Cast strings to numbers | Feature encoding and data cleaning |
| Boolean checks (`is_saturated`) | Filtering datasets, creating target labels |
| SPT correlations (N60, Vs) | Feature engineering for prediction models |
| Formatted report | Model output / Streamlit dashboard display |

---

## 3 Key Takeaways

1. **Variables** are named containers. Use clear names like `spt_n_value` instead of `x`. Your future self (and your ML pipeline) will thank you.

2. **Data types matter**. `int` for counts, `float` for measurements, `str` for descriptions, `bool` for yes/no conditions. Field data almost always arrives as strings — you must cast before calculating.

3. **f-strings are your best friend**. Write `f"N60 = {N60:.1f}"` instead of `"N60 = " + str(round(N60, 1))`. Cleaner, faster, fewer bugs.

---

## Resources

- [Python Official Tutorial — Numbers](https://docs.python.org/3/tutorial/introduction.html#numbers)
- [Python Official Tutorial — Strings](https://docs.python.org/3/tutorial/introduction.html#strings)
- [f-strings Guide (Real Python)](https://realpython.com/python-f-strings/)
- [SPT Correlations — Imai & Tonouchi (1982)](https://scholar.google.com/scholar?q=Imai+Tonouchi+1982+shear+wave+velocity)

---

*Day 001 of 100 — The journey begins!*
