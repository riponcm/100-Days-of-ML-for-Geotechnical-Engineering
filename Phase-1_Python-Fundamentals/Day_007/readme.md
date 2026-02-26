# Day 007 | Functions & Lambda Expressions

**100 Days of ML for Geotechnical Engineering** | Phase 1: Python Fundamentals
Author: Ripon Chandra Malo | Date: February 22, 2026

---

## Geotechnical Problem We Solved Today

We kept copy-pasting the same SPT calculations across Days 001-006. Functions solve this: **write once, call forever.** We built a reusable SPT Analysis Toolkit and used it for 3 mini-projects: borehole processor, bearing capacity calculator, and multi-borehole site comparator.

---

## Concept 1: Defining & Calling Functions

```python
# DEFINE (build the machine)
def classify_granular(N60):           # def + name + parameter + colon
    """Classify soil from N60."""      # docstring
    if N60 < 4: return "Very Loose"   # function body
    elif N60 < 10: return "Loose"
    elif N60 < 30: return "Medium Dense"
    elif N60 < 50: return "Dense"
    else: return "Very Dense"

# CALL (use the machine)
result = classify_granular(22)        # → "Medium Dense"
```

Defining does NOT run the code. Calling (with parentheses) does.

---

## Concept 2: Parameters & Arguments

```python
def estimate_vs(N60):        # N60 is the PARAMETER (slot)
    return 97 * (N60 ** 0.314)

estimate_vs(22)              # 22 is the ARGUMENT (actual value)
```

**Parameter** = placeholder in definition. **Argument** = actual value in call.

---

## Concept 3: Return Values

`return` sends a result back. Without it, the function returns `None`.

```python
def calc_vs(N60):
    return 97 * (N60 ** 0.314)    # Sends value back

Vs = calc_vs(22)                   # Vs = 256.0

# Without return → result = None !
```

---

## Concept 4: Default Parameters

Pre-set values that can be overridden. Like a form with pre-filled fields.

```python
def simple_n60(N_field, efficiency=60, diameter=100):
    ...

simple_n60(22)                     # uses defaults
simple_n60(22, efficiency=80)      # overrides efficiency
simple_n60(22, diameter=200)       # overrides diameter
```

**Rule:** Required params first, then optional with defaults.

---

## Concept 5: Multiple Return Values

```python
def analyze(N_field, depth, wt):
    N60 = N_field * 1.0
    Vs = 97 * (N60 ** 0.314)
    sat = depth > wt
    return N60, Vs, sat             # Returns tuple

N60, Vs, sat = analyze(22, 6.5, 3.2)  # Unpack all three
```

---

## Concept 6: Returning Dictionaries

For complex results — access by name instead of remembering order:

```python
def full_analysis(N60, depth):
    return {
        "N60": N60,
        "Vs": round(97 * N60**0.314, 1),
        "consistency": classify(N60),
    }

result = full_analysis(22, 6.0)
result["Vs"]           # Clear! No index guessing.
```

---

## Concept 7: Docstrings (NumPy Style)

```python
def bearing_capacity(N60, Df, B):
    """
    Allowable bearing capacity from SPT.
    
    Parameters
    ----------
    N60 : float — Corrected blow count
    Df : float — Foundation depth (m)
    B : float — Foundation width (m)
    
    Returns
    -------
    float — Allowable bearing capacity (kPa)
    """
```

Access with `help(bearing_capacity)` or `bearing_capacity.__doc__`

---

## Concept 8: Variable Scope

- **Local** variables (inside function) → die when function ends
- **Global** variables (outside) → accessible everywhere

```python
project = "Bridge"        # GLOBAL

def calc(N60, load):
    factor = 0.1          # LOCAL — only exists here
    return factor * load / N60

print(project)   # Works
# print(factor)  # NameError! factor is local
```

---

## Concept 9: Lambda — One-Line Functions

```python
# Regular (3 lines)              # Lambda (1 line)
def vs(N60):                      vs = lambda N60: 97 * (N60 ** 0.314)
    return 97 * (N60 ** 0.314)

# Most common use: SORT KEY
sorted(layers, key=lambda d: d["N60"])            # Sort dicts by N60
sorted(layers, key=lambda d: d["depth"])           # Sort by depth
sorted(layers, key=lambda d: d["N60"], reverse=True)  # Descending
```

**Rule:** Simple calculation → lambda. Complex logic → `def`.

---

## Concept 10: Function Pipelines

Small functions chained together:

```python
N60 = correct_n(22)           # Step 1
Vs = calc_vs(N60)             # Step 2 (uses Step 1 output)
cons = classify(N60)          # Step 3
sigma_v = calc_overburden(6)  # Step 4
```

This IS how ML pipelines work: preprocess → train → evaluate.

---

## Mini Projects Built Today

1. **SPT Borehole Processor** — `process_borehole()` takes raw field data, returns processed layers + summary dict
2. **Bearing Capacity Calculator** — `bearing_meyerhof()` + `safety_check()` for multiple design scenarios
3. **Multi-Borehole Comparator** — Process 3 boreholes with ONE function, generate comparison table

---

## 3 Key Takeaways

1. **Functions = reusability.** `classify_granular(22)` replaces 10 lines of if/elif. Write once, call 1000 times. If you find a bug, fix it in ONE place.

2. **Return dictionaries** for complex results — `result["Vs"]` is self-documenting. No remembering that Vs was the 3rd return value in a tuple.

3. **Function pipelines** (small functions chained) are how real engineering software and ML pipelines are built. Each function does ONE thing well. Together they do everything.

---

## How This Connects to ML

| Today | ML Equivalent |
|-------|---------------|
| `def function()` | Custom loss functions, preprocessing |
| Parameters | Hyperparameters (`learning_rate`) |
| Default params | `RandomForest(n_estimators=100)` |
| Return dict | `model.evaluate()` → `{"loss": ..., "acc": ...}` |
| Lambda sort key | Pandas `.sort_values()` |
| Function pipeline | `sklearn.Pipeline([preprocess, model])` |

Every ML library is just a collection of functions. Today you learned to build your own.

---

*Day 007 of 100 — We now have a reusable geotechnical toolkit!*
