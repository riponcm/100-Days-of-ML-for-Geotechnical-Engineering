# Day 009 | Error Handling — try / except / finally

**100 Days of ML for Geotechnical Engineering** | Phase 1: Python Fundamentals
Author: Ripon Chandra Malo | Date: February 24, 2026

---

## Geotechnical Problem We Solved Today

Real field data is messy — "NR" instead of numbers, blank cells, wrong formats. Without error handling, one bad row crashes the entire script. We learned to catch errors, skip bad rows, log problems, and keep processing.

---

## Concept 1: try / except — The Basic Pattern

```python
try:
    n = int("NR")          # might fail
except ValueError:
    n = 0                   # safe fallback
```

`try` = attempt risky code. `except` = catch specific error.

---

## Concept 2: Catch SPECIFIC Errors

```python
except ValueError:          # bad conversion ("NR" → int)
except ZeroDivisionError:   # divide by zero (N60=0)
except FileNotFoundError:   # missing file
except KeyError:            # wrong dict key
except IndexError:          # list index out of range
```

**Never** use bare `except:` — it hides real bugs.

---

## Concept 3: else and finally

```python
try:
    data = load_file()         # risky
except FileNotFoundError:
    print("Missing!")          # on error
else:
    process(data)              # on SUCCESS only
finally:
    save_log()                 # ALWAYS runs
```

`finally` is for cleanup — saving logs, closing connections.

---

## Concept 4: raise — Your Own Errors

```python
if N60 < 0:
    raise ValueError("N60 cannot be negative!")
if N60 > 100:
    raise ValueError("N60 too high — check data")
```

Python won't catch engineering impossibilities. You add that check yourself.

---

## Concept 5: Skip Bad, Keep Good (THE Key Pattern)

```python
good = []
errors = []

for i, row in enumerate(raw_data, 1):
    try:
        result = process(row)     # might fail
        good.append(result)       # save if good
    except (ValueError, KeyError) as e:
        errors.append(f"Row {i}: {e}")  # log if bad

print(f"{len(good)} good, {len(errors)} errors")
```

The `try/except` is **inside** the loop. Each row gets its own chance.

---

## Complete Pipeline Built Today

```
messy_field_data.csv → [try/except each row] → clean_results.csv
                                              → error_log.txt
```

Input: 8 rows with "NR", blank, and "6.0m" errors.
Output: 6 clean rows + 2 logged errors.

---

## 3 Key Takeaways

1. **`try/except` is a safety net.** Risky operations (file reading, type conversion, division) go inside `try`. The program survives instead of crashing.

2. **"Skip bad, keep good"** is the #1 real-world pattern. Wrap each row in `try/except` inside a loop. One bad row doesn't kill the other 999.

3. **`raise`** adds engineering validation: reject N60 > 100, negative depths, or impossible values that Python wouldn't catch on its own.

---

## How This Connects to ML

| Today | ML Equivalent |
|-------|---------------|
| `try/except` | Handling corrupt images, bad CSV rows |
| `raise ValueError` | Input validation in `model.fit()` |
| Skip bad rows | `errors='coerce'` in `pd.to_numeric()` |
| Error logging | TensorBoard, MLflow tracking |
| `finally` cleanup | Releasing GPU memory, saving checkpoints |

---

*Day 009 of 100 — Our code is now crash-proof!*
