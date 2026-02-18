# Day 003 | Loops — for, while, enumerate, zip

**100 Days of ML for Geotechnical Engineering**
Phase 1: Python Fundamentals
Author: Ripon Chandra Malo
Date: February 18, 2026

---

## Geotechnical Problem We Solved Today

We had **8 layers of SPT data** from BH-01. Instead of writing the same classification code 8 times, we used **loops** to write it once and apply it to every layer automatically. Then we processed multiple boreholes and generated a complete automated report with statistics.

This is the core of all data processing — whether 8 rows or 8 million.

---

## Concept 1: for Loop

Repeat code **once for each item** in a collection.

```python
for item in collection:
    # do something with item
```

### Geotechnical Example

```python
n_values = [5, 8, 12, 18, 28, 35, 50, 60]

for n in n_values:
    if n < 10:
        print(f"N={n}: Loose")
    elif n < 30:
        print(f"N={n}: Medium Dense")
    else:
        print(f"N={n}: Dense+")
```

The loop runs 8 times — once per N-value. The variable `n` changes each iteration.

---

## Concept 2: range()

Generates number sequences for looping.

| Syntax | Result | Use Case |
|--------|--------|----------|
| `range(5)` | 0, 1, 2, 3, 4 | Loop 5 times |
| `range(2, 7)` | 2, 3, 4, 5, 6 | Start from 2 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 | Every other item |
| `range(3, 0, -1)` | 3, 2, 1 | Count down |

### Geotechnical Example: Generating Depth Intervals

```python
for i in range(8):
    depth = 1.5 * (i + 1)    # produces 1.5, 3.0, 4.5, ... 12.0
    print(f"Sample {i+1}: {depth:.1f} m")
```

---

## Concept 3: while Loop

Repeats **as long as a condition is True**. Use when you don't know how many iterations you need.

```python
while condition:
    # do something
    # condition must eventually become False!
```

### When to Use for vs while

| Use `for` | Use `while` |
|-----------|-------------|
| Known number of iterations | Unknown when to stop |
| Iterating through a list | Waiting for a condition |
| "Process each layer" | "Keep drilling until refusal" |

### Geotechnical Example: Drilling Until Refusal

```python
depth = 0.0
while depth < 30.0:
    depth += 1.5
    n = get_n_value(depth)
    if n >= 50:
        print(f"Refusal at {depth}m!")
        break
```

### Infinite Loop Warning

If the condition never becomes False, the loop runs forever. Always ensure something changes inside the loop. Press **Ctrl+C** or click the stop button if you accidentally create one.

---

## Concept 4: enumerate()

Get the **index AND value** together. No need for `range(len(...))` hack.

```python
# Without enumerate (clunky):
for i in range(len(soils)):
    print(f"Layer {i}: {soils[i]}")

# With enumerate (clean):
for i, soil in enumerate(soils):
    print(f"Layer {i}: {soil}")

# Start counting from 1 (engineering style):
for num, soil in enumerate(soils, start=1):
    print(f"Layer {num}: {soil}")
```

### When to Use

- Numbered reports (Layer 1, Layer 2, ...)
- Calculating depth from index: `depth = 1.5 * (i + 1)`
- Accessing items from another list by index

---

## Concept 5: zip()

Pair items from **multiple lists** that represent the same data at each position.

```python
depths =     [1.5, 3.0, 4.5]
n_values =   [5,   8,   12]
soil_types = ["Fill", "Sand", "Clay"]

for d, n, s in zip(depths, n_values, soil_types):
    print(f"{d}m: N={n}, {s}")

# Output:
# 1.5m: N=5, Fill
# 3.0m: N=8, Sand
# 4.5m: N=12, Clay
```

### The Ultimate Combo: enumerate + zip

```python
for i, (d, n, s) in enumerate(zip(depths, n_values, soil_types), start=1):
    print(f"Layer {i}: {d}m | N={n} | {s}")
```

This gives you: layer number + depth + N-value + soil type — all in one line. This pattern appears in almost every data processing script.

---

## Concept 6: Loop Control

| Keyword | Action | Example |
|---------|--------|---------|
| `break` | Stop the loop immediately | Stop at first bearing layer |
| `continue` | Skip this iteration, go to next | Skip non-sandy layers |
| `pass` | Do nothing (placeholder) | TODO: add calculation later |

### break — Find First Bearing Layer

```python
for d, n in zip(depths, n_values):
    if n >= 15:
        print(f"Bearing layer at {d}m")
        break    # Stop searching
```

### continue — Check Only Sandy Layers

```python
for d, n, s in zip(depths, n_values, soil_types):
    if "Sand" not in s:
        continue    # Skip to next layer
    # Only sandy layers reach here
    print(f"{d}m: N={n}, {s}")
```

---

## Concept 7: Accumulator Patterns

The building blocks of computing statistics from loops.

| Pattern | Initialize | Update Inside Loop | Result |
|---------|-----------|-------------------|--------|
| Sum | `total = 0` | `total += n` | Total of all values |
| Count | `count = 0` | `if cond: count += 1` | How many meet condition |
| Average | sum + count | — | `total / count` |
| Min | `mn = first` | `if n < mn: mn = n` | Smallest value |
| Max | `mx = first` | `if n > mx: mx = n` | Largest value |
| Build list | `result = []` | `result.append(x)` | New computed list |

### Example: All Patterns at Once

```python
n_values = [5, 8, 12, 18, 28, 35, 50, 60]
total = 0
n_min = n_values[0]
n_max = n_values[0]
weak = 0
vs_list = []

for n in n_values:
    total += n
    if n < n_min: n_min = n
    if n > n_max: n_max = n
    if n < 15: weak += 1
    vs_list.append(97 * n**0.314)

avg = total / len(n_values)
```

In Phase 2, NumPy replaces all of this with `np.mean()`, `np.min()`, etc. But understanding the loop version teaches you what those functions do internally.

---

## Complete Application: What We Built

An automated borehole report that processes 8 layers using:

| Tool | Purpose |
|------|---------|
| `for` loop | Process every layer |
| `enumerate` | Layer numbering |
| `zip` | Pair depth + N + soil type |
| `if/elif/else` | Classify consistency |
| Comparison | Saturation check |
| Logical `and` | Liquefaction screening |
| Ternary | Quick status flags |
| Accumulators | Sum, average, min, max, Vs list |
| `break` logic | Find first bearing layer |

All of Day 001 + Day 002 + Day 003 combined into one 30-line script that replaces manual Excel work.

---

## 3 Key Takeaways

1. **for loops** process collections item by item. Write the logic once, apply to all data. Whether 8 layers or 8 million rows, same code.

2. **enumerate + zip** is the most common pattern in data processing. `enumerate` gives you numbering, `zip` pairs parallel data. Combined, they give you everything: `for i, (d, n, s) in enumerate(zip(...))`.

3. **Accumulator patterns** (sum, count, min, max, build list) are the manual version of NumPy/Pandas functions. Every ML training loop uses accumulators to track loss and accuracy across epochs.

---

## How This Connects to ML

| Today's Concept | ML Equivalent |
|----------------|---------------|
| `for` through layers | Iterating through dataset rows |
| `while` until condition | Training loop (`while loss > threshold`) |
| `enumerate` | Batch indexing in PyTorch DataLoader |
| `zip(X, y)` | Pairing features and labels |
| Accumulator (avg) | Computing loss per epoch |
| `break` | Early stopping when validation loss plateaus |
| Nested loops | Grid search: `for lr in [...]: for batch in [...]` |

The PyTorch training loop is literally:

```python
for epoch in range(100):
    for X_batch, y_batch in dataloader:
        loss = model(X_batch, y_batch)
        loss.backward()
```

---

## Resources

- [Python for Loops (W3Schools)](https://www.w3schools.com/python/python_for_loops.asp)
- [enumerate() Explained (Real Python)](https://realpython.com/python-enumerate/)
- [zip() Guide (Real Python)](https://realpython.com/python-zip-function/)
- [Python while Loops (W3Schools)](https://www.w3schools.com/python/python_while_loops.asp)

---

*Day 003 of 100 — Python can now process entire boreholes automatically!*
