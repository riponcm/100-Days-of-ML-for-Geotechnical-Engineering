# Day 005 | Lists, Tuples & Sets

**100 Days of ML for Geotechnical Engineering** | Phase 1: Python Fundamentals
Author: Ripon Chandra Malo | Date: February 20, 2026

---

## Geotechnical Problem We Solved Today

Borehole data is fundamentally a **collection** of values. We need different container types depending on whether the data changes, needs ordering, or must be unique:

```
Depths:      [1.5, 3.0, 4.5, ...]       ← grows as drilling continues  → LIST
Sieve sizes: (75.0, 19.0, 4.75, ...)    ← fixed engineering standard   → TUPLE
Soil types:  {"Sand", "Clay", "Gravel"}  ← unique types at site         → SET
```

We built a **complete data pipeline** that uses all three: lists for field data, tuples for site constants, sets for unique soil identification, and list comprehension for one-line data transformation.

---

## Concept 1: Lists `[]` — Ordered, Mutable

A list is an ordered collection that can grow, shrink, and change.

### Creating

```python
n_values = [5, 8, 12, 18, 28, 35, 50, 60]   # from values
empty = []                                      # empty, fill later
from_range = list(range(1, 9))                  # [1, 2, 3, ..., 8]
```

### Indexing & Slicing

```
List:     [5,   8,   12,  18,  28,  35,  50,  60]
Index:     0    1    2    3    4    5    6    7
Negative: -8   -7   -6   -5   -4   -3   -2   -1
```

| Syntax | Result | Meaning |
|--------|--------|---------|
| `l[0]` | `5` | First item |
| `l[-1]` | `60` | Last item |
| `l[:3]` | `[5, 8, 12]` | First 3 |
| `l[-3:]` | `[35, 50, 60]` | Last 3 |
| `l[2:5]` | `[12, 18, 28]` | Index 2, 3, 4 |
| `l[::2]` | `[5, 12, 28, 50]` | Every 2nd |
| `l[::-1]` | `[60, 50, ...]` | Reversed |

### Key Methods

| Method | What It Does | Example |
|--------|-------------|---------|
| `.append(x)` | Add ONE to end | `data.append(22)` |
| `.extend([x,y])` | Add MULTIPLE | `data.extend([35, 50])` |
| `.insert(i, x)` | Insert at position | `data.insert(0, 2)` |
| `.pop(i)` | Remove & return at i | `data.pop(0)` |
| `.pop()` | Remove & return last | `data.pop()` |
| `.remove(x)` | Remove first x | `data.remove(8)` |
| `.sort()` | Sort in place | `data.sort()` |
| `.count(x)` | Count occurrences | `data.count(8)` |
| `.index(x)` | Find position | `data.index(22)` |

### Built-in Functions

```python
len(data)   # 8 layers
min(data)   # 5 (weakest)
max(data)   # 60 (strongest)
sum(data)   # 216
sum(data)/len(data)  # 27.0 (average)
sorted(data)         # returns NEW sorted list (original unchanged)
```

---

## Concept 2: List Comprehension — The Pythonic Superpower

One-line loop that creates a new list by transforming each item.

### Basic Syntax

```python
# Traditional loop (4 lines)          # Comprehension (1 line!)
result = []                            result = [97 * n**0.314 for n in n_values]
for n in n_values:
    result.append(97 * n**0.314)
```

### With Condition (Filtered)

```python
# [expression FOR variable IN iterable IF condition]
strong = [n for n in n_values if n >= 20]           # Only strong layers
sandy_n = [n for n, s in zip(n_values, soils) if "Sand" in s]  # Sandy only
```

### Common Patterns

```python
vs = [97 * (n ** 0.314) for n in n_values]          # Transform all
sigma_v = [18.5 * d for d in depths]                 # Simple formula
labels = ["Weak" if n < 15 else "Strong" for n in n_values]  # Classify
n_strings = [str(n) for n in n_values]               # Convert types
count = len([n for n in n_values if n < 15])         # Count filtered
```

---

## Concept 3: Tuples `()` — Ordered, Immutable

Like a list but **cannot be changed** after creation. Protects data from accidental modification.

```python
# Create
coords = (40.7608, -111.8910, 1320.5)    # parentheses
sieve_sizes = (75.0, 19.0, 4.75, 2.0, 0.425, 0.075)

# Access (same as lists)
coords[0]     # 40.7608
coords[-1]    # 1320.5

# Unpack
lat, lon, elev = coords

# CANNOT modify
coords[0] = 41.0           # TypeError!
coords.append(something)   # AttributeError!
```

### When to Use Tuple vs List

| Data changes or grows? | → **List** | SPT readings, field measurements |
|------------------------|-----------|----------------------------------|
| Data should stay fixed? | → **Tuple** | Coordinates, sieve sizes, standards |
| Returning multiple values? | → **Tuple** | `return (N60, Vs, consistency)` |

---

## Concept 4: Sets `{}` — Unordered, Unique Only

A set stores only **unique** values. Duplicates are automatically removed.

### Creating

```python
unique_soils = set(["Sand", "Clay", "Sand", "Gravel", "Sand"])
# Result: {"Sand", "Clay", "Gravel"}  — duplicates gone!

direct_set = {"Sand", "Clay", "Gravel"}    # Curly braces
```

### Set Operations — Comparing Boreholes

| Operation | Symbol | Meaning | Geotech Example |
|-----------|--------|---------|-----------------|
| Union | `A \| B` | Everything in A or B | All soil types at site |
| Intersection | `A & B` | Only in BOTH | Common soils across boreholes |
| Difference | `A - B` | In A but NOT B | Soils unique to BH-01 |
| Symmetric Diff | `A ^ B` | In one but not both | Soils exclusive to each |
| Membership | `x in A` | Is x in the set? | `"Sand" in site_soils` |

### Practical Uses

```python
# Remove duplicates
unique_ids = sorted(set(field_log_ids))

# Validate entries
invalid = entered_soils - allowed_soils

# Track progress
remaining = planned_depths - tested_depths
progress = len(tested) / len(planned) * 100
```

**Important:** Sets are **unordered** — no indexing (`my_set[0]` causes TypeError). Convert to `sorted(list(my_set))` if you need order.

---

## Complete Collection Comparison

| Feature | List `[]` | Tuple `()` | Set `{}` |
|---------|-----------|------------|----------|
| **Ordered** | Yes | Yes | No |
| **Mutable** | Yes | No | Yes (add/remove) |
| **Duplicates** | Allowed | Allowed | Not allowed |
| **Indexing** | `l[0]` | `t[0]` | Not possible |
| **Create** | `[1, 2, 3]` | `(1, 2, 3)` | `{1, 2, 3}` |
| **Convert** | `list(x)` | `tuple(x)` | `set(x)` |
| **Best for** | Data that grows | Constants | Unique values |

---

## 3 Key Takeaways

1. **Lists** are the workhorse — ordered, mutable, support indexing/slicing. Use `.append()` to build data incrementally, comprehension to transform it in one line.

2. **Tuples** protect constants from accidental changes. Use for coordinates, sieve sizes, and any data that should never be modified after creation.

3. **Sets** find unique values instantly and support powerful comparison operations (union, intersection, difference). Perfect for data validation, duplicate removal, and comparing boreholes.

---

## How This Connects to ML

| Today | ML Equivalent |
|-------|---------------|
| Lists of N-values | NumPy arrays, Pandas Series |
| List comprehension | `df.apply()`, vectorized operations |
| Filtered `[if]` | `df[df['N60'] > 20]` boolean indexing |
| Nested lists (2D) | Feature matrices `X`, 2D arrays |
| Tuples | Dataset shapes `(rows, cols)`, immutable configs |
| Sets (unique) | `df['soil'].unique()`, label sets |
| Set operations | Train/test split verification |

---

*Day 005 of 100 — We now have three data containers for every situation!*
