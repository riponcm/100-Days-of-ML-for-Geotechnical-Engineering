# Day 006 | Dictionaries & Comprehensions

**100 Days of ML for Geotechnical Engineering** | Phase 1: Python Fundamentals
Author: Ripon Chandra Malo | Date: February 21, 2026

---

## Geotechnical Problem We Solved Today

Parallel lists (`depths[3]`, `n_values[3]`, `soils[3]`) are fragile — one wrong index pairs wrong data. Dictionaries solve this by using **names** instead of positions: `layer["N60"]` is crystal clear.

We built a **multi-borehole site database** with nested dictionaries, lookup tables for soil properties and USCS classifications, and generated a cross-borehole comparison report — all using named access instead of index guessing.

---

## Concept 1: Creating Dictionaries

```python
# Key-value pairs in curly braces
layer = {"depth": 6.0, "N60": 18, "soil": "Clayey Sand"}

# From two lists
layer = dict(zip(["depth", "N60", "soil"], [6.0, 18, "Sand"]))

# Empty, fill later
record = {}
record["project"] = "Bridge"
```

**Rules:** Keys must be immutable & unique. Values can be anything.

---

## Concept 2: Accessing Values

| Method | If Key Missing | Example |
|--------|---------------|---------|
| `d["key"]` | **KeyError** (crash) | `layer["N60"]` → `18` |
| `d.get("key")` | Returns `None` | `layer.get("color")` → `None` |
| `d.get("key", default)` | Returns default | `layer.get("color", "N/A")` → `"N/A"` |
| `"key" in d` | — | `"N60" in layer` → `True` |

**Always use `.get()` for fields that might be missing** — prevents crashes in real data.

---

## Concept 3: Modifying Dictionaries

```python
layer["Vs"] = 240.4           # ADD new key
layer["N60"] = 20             # UPDATE existing
del layer["color"]            # DELETE
vs = layer.pop("Vs")          # REMOVE and return
layer.update({"Vs": 245, "Dr": 65})  # UPDATE multiple
```

---

## Concept 4: Looping — keys, values, items

```python
for key in layer:                     # Keys only
for value in layer.values():          # Values only
for key, value in layer.items():      # Both (most common)
```

---

## Concept 5: Nested Dictionaries

Dicts inside dicts for complex, hierarchical data:

```python
borehole = {
    "id": "BH-01",
    "location": {"lat": 40.76, "lon": -111.89, "city": "SLC"},
    "layers": [
        {"depth": 1.5, "N60": 5, "soil": "Fill"},
        {"depth": 3.0, "N60": 8, "soil": "Sand"},
    ]
}

# Chain keys to access nested data
borehole["location"]["city"]     # "SLC"
borehole["layers"][0]["N60"]     # 5
```

---

## Concept 6: List of Dictionaries — THE Data Pattern

```python
layers = [
    {"depth": 1.5, "N60": 5,  "soil": "Fill"},       # Row 1
    {"depth": 3.0, "N60": 8,  "soil": "Sand"},       # Row 2
    {"depth": 6.0, "N60": 18, "soil": "Clay"},       # Row 3
]

# Extract a "column"
all_n = [l["N60"] for l in layers]

# Filter "rows"
sandy = [l for l in layers if "Sand" in l["soil"]]
```

This is **exactly** how `pd.DataFrame(layers)` works in Pandas.

---

## Concept 7: Lookup Tables

Replace if/elif chains with instant dictionary access:

```python
soil_weight = {"Sand": 18.5, "Clay": 17.0, "Gravel": 20.0}
gamma = soil_weight["Sand"]    # Instant! No searching.
gamma = soil_weight.get(soil_type, 18.0)  # Safe with default
```

---

## Concept 8: Dictionary Comprehension

One-line dict creation (like list comprehension but for dicts):

```python
# {key_expr: val_expr for var in iterable}
depth_to_n = {d: n for d, n in zip(depths, n_values)}
depth_to_vs = {d: round(97*(n**0.314), 1) for d, n in zip(depths, n_values)}

# With filter
sat_n = {d: n for d, n in zip(depths, n_values) if d > 3.2}

# Invert a dict
uscs_to_soil = {v: k for k, v in soil_to_uscs.items()}
```

---

## Concept 9: Counting & Grouping

```python
# Counting with .get()
count = {}
for soil in all_soils:
    count[soil] = count.get(soil, 0) + 1

# Grouping
groups = {}
for layer in layers:
    cls = classify(layer["N60"])
    if cls not in groups:
        groups[cls] = []
    groups[cls].append(layer)
```

---

## 3 Key Takeaways

1. **Dictionaries use names, not positions.** `layer["N60"]` is self-documenting — no guessing what index 3 means across parallel lists.

2. **`.get(key, default)` prevents crashes** from missing data — essential for real-world datasets. Always use it when a field might not exist.

3. **List of dictionaries → Pandas DataFrame.** The pattern `[{"col1": val, "col2": val}, ...]` converts directly to a DataFrame with `pd.DataFrame(data)`. Everything we built today is the exact input format for Phase 2.

---

## How This Connects to ML

| Today | ML Equivalent |
|-------|---------------|
| Dictionary | JSON data, model configs, hyperparams |
| `d["key"]` | `df["column_name"]` in Pandas |
| List of dicts | `pd.DataFrame(list_of_dicts)` |
| Lookup table | Label encoding, feature mapping |
| Dict comprehension | Feature engineering |
| Counting | `df["col"].value_counts()` |
| Grouping | `df.groupby("class")` |
| Nested dicts | JSON API responses, model metadata |

---

*Day 006 of 100 — Dictionaries give us labeled, structured data!*
