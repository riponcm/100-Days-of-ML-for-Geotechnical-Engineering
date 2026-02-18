# Day 002 | Conditionals — if / elif / else

**100 Days of ML for Geotechnical Engineering**
Phase 1: Python Fundamentals
Author: Ripon Chandra Malo
Date: February 17, 2026

---

## Geotechnical Problem We Solved Today

We wrote **automated decision-making logic** for a borehole safety assessment in Salt Lake City. The Python code now does what a geotechnical engineer does when reading a borehole log:

1. Classifies soil consistency from SPT N60 values
2. Checks if each layer is saturated
3. Screens every layer for liquefaction risk
4. Verifies bearing capacity safety
5. Generates a complete multi-layer safety report

This is the foundation of all ML classification — **making decisions based on conditions**.

---

## Concept 1: Basic if / else

The simplest decision — two outcomes.

```python
if condition:
    # runs when True
else:
    # runs when False
```

### Geotechnical Example: Saturation Check

```python
water_table = 3.2
sample_depth = 6.5

if sample_depth > water_table:
    print("Saturated")    # This runs (6.5 > 3.2 is True)
else:
    print("Dry")
```

**Key rules:**
- Colon `:` after every `if` and `else`
- Code inside must be **indented** (4 spaces)
- The condition evaluates to `True` or `False`

---

## Concept 2: if / elif / else

When there are more than two outcomes. Python checks top-to-bottom and **stops at the first True**.

```python
if condition_1:
    # runs if condition_1 is True
elif condition_2:
    # runs if condition_1 was False AND condition_2 is True
elif condition_3:
    # runs if both above were False AND condition_3 is True
else:
    # runs if ALL above were False
```

### Geotechnical Example: Soil Consistency (Granular)

| N60 Range | Consistency |
|-----------|-------------|
| < 4 | Very Loose |
| 4 – 9 | Loose |
| 10 – 29 | Medium Dense |
| 30 – 49 | Dense |
| >= 50 | Very Dense |

```python
if N60 < 4:
    consistency = "Very Loose"
elif N60 < 10:
    consistency = "Loose"
elif N60 < 30:
    consistency = "Medium Dense"
elif N60 < 50:
    consistency = "Dense"
else:
    consistency = "Very Dense"
```

**How it works for N60 = 22:**
1. Is 22 < 4? No → skip
2. Is 22 < 10? No → skip
3. Is 22 < 30? **Yes** → set "Medium Dense" → **STOP** (skip the rest)

**Important:** Order matters! Put the smallest range first.

---

## Concept 3: Comparison Operators

These produce `True` or `False` — the inputs to every `if` statement.

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `soil == "Clay"` | True/False |
| `!=` | Not equal | `status != "Failed"` | True/False |
| `>` | Greater than | `load > capacity` | True if overstressed |
| `<` | Less than | `FoS < 1.5` | True if unsafe |
| `>=` | Greater or equal | `N60 >= 50` | True if refusal |
| `<=` | Less or equal | `depth <= wt` | True if above water table |

### Common Mistake

| Wrong | Right | Why |
|-------|-------|-----|
| `if x = 5:` | `if x == 5:` | `=` assigns, `==` compares |

---

## Concept 4: Logical Operators

Combine multiple conditions into one check.

| Operator | Meaning | True When |
|----------|---------|-----------|
| `and` | Both must be true | `sat and N60 < 20` — both needed |
| `or` | At least one true | `N60 < 4 or organic` — either flags it |
| `not` | Flip the result | `not is_saturated` — means "is it dry?" |

### Geotechnical Example: Liquefaction Screening

Liquefaction requires ALL conditions true:

```python
if is_saturated and is_sandy and (N60 < 20) and seismic_zone:
    print("Liquefaction analysis required!")
```

Using `or` for flagging layers needing attention (any one problem is enough):

```python
if (N60 < 4) or is_organic or (depth < 1.5):
    print("Layer needs special attention")
```

### Truth Table

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| True | True | True | True | False |
| True | False | False | True | False |
| False | True | False | True | True |
| False | False | False | False | True |

---

## Concept 5: Nested if

Put one `if` inside another for step-by-step reasoning. Mimics how engineers think through a problem.

```python
if earthquake_zone:
    if soil_type == "Sand":
        if is_saturated:
            if N60 < 20:
                print("LIQUEFACTION RISK: HIGH")
```

**When to use nested vs flat:**
- **Flat** (`and` in one line): Quick check, all conditions equal weight
- **Nested**: Step-by-step screening, want to show reasoning chain

---

## Concept 6: Ternary Operator

One-line shortcut for simple if/else:

```python
result = "value_if_true" if condition else "value_if_false"
```

### Examples

```python
status = "Suitable" if N60 >= 15 else "Not Suitable"
condition = "Saturated" if depth > wt else "Dry"
safety = "SAFE" if FoS >= 1.5 else "UNSAFE"
```

Use for simple assignments. For complex logic, use regular if/elif/else.

---

## Complete Application: What We Built

A multi-layer borehole assessment that processes 6 soil layers and for each one:

| Check | Method Used | Output |
|-------|------------|--------|
| Consistency | if/elif/else | Very Loose to Very Dense |
| Saturation | comparison + ternary | Yes / No |
| Liquefaction | logical operators (and) | CHECK / OK |
| Foundation | ternary | Yes / No |
| Safety summary | if/else with counter | Warnings + recommendations |

---

## 3 Key Takeaways

1. **if/elif/else** checks conditions top-to-bottom and runs only the first True block. This is exactly how Decision Trees work in ML — the same logic you wrote by hand today, ML models learn automatically from data.

2. **Logical operators** (`and`, `or`, `not`) combine conditions. `and` requires all true (strict screening), `or` requires any one true (broad flagging). This becomes critical for data filtering in Pandas and feature engineering.

3. **Every engineering classification table** (soil consistency, site class, FoS categories) translates directly into an if/elif/else chain. When you have thousands of samples, you let ML learn these boundaries from data instead of coding them by hand — that's classification.

---

## How This Connects to ML

| What We Did Today | ML Equivalent (Phase 3-5) |
|-------------------|-----------------------------|
| if/elif/else chains | Decision Tree classifier |
| Nested decisions | Random Forest (many trees) |
| Threshold comparisons | Split points in tree nodes |
| and/or for filtering | Pandas boolean indexing |
| Classification from N60 | Supervised classification from features |
| Ternary for labels | Creating target variable (y) |

---

## Resources

- [Python if/elif/else (W3Schools)](https://www.w3schools.com/python/python_conditions.asp)
- [Comparison Operators (Real Python)](https://realpython.com/python-operators-expressions/)
- Terzaghi & Peck — Soil consistency classification tables
- Seed & Idriss (1971) — Simplified liquefaction procedure

---

*Day 002 of 100 — Now Python thinks like a geotechnical engineer!*
