# Day 008 | File I/O — Read & Write CSV, TXT

**100 Days of ML for Geotechnical Engineering** | Phase 1: Python Fundamentals
Author: Ripon Chandra Malo | Date: February 23, 2026

---

## Geotechnical Problem We Solved Today

Real data lives in FILES, not hardcoded lists. We learned to read borehole CSVs from the drilling company, process them in Python, and write analysis reports back — the complete field-to-report pipeline.

---

## Concept 1: The `with` Statement — Safe File Handling

```python
# ALWAYS use this pattern:
with open("data.csv", "r") as f:
    content = f.read()
# File auto-closes here — even if an error occurs!
```

Never use `open()`/`close()` manually — forgetting `close()` can lose data.

---

## Concept 2: File Modes

| Mode | Meaning | Existing file | No file |
|------|---------|--------------|---------|
| `"r"` | Read | Opens it | Error! |
| `"w"` | Write | **Overwrites!** | Creates new |
| `"a"` | Append | Adds to end | Creates new |

⚠️ `"w"` erases the file! Use `"a"` to add without erasing.

---

## Concept 3: Reading Text Files

```python
# Entire file as one string
content = f.read()

# List of all lines
lines = f.readlines()

# One line at a time (BEST for large files)
for line in f:
    print(line.strip())
```

---

## Concept 4: Writing CSV — csv.writer

```python
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Depth", "N60", "Soil"])    # header
    writer.writerow([1.5, 5, "Fill"])             # data row
```

---

## Concept 5: Reading CSV — csv.DictReader (THE BEST)

Each row becomes a dictionary — access by column NAME:

```python
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        depth = float(row["Depth"])   # Convert string → number!
        n60 = int(row["N60"])
```

⚠️ All CSV values are STRINGS. Always convert with `int()` / `float()`.

---

## Concept 6: DictWriter — List of Dicts → CSV

```python
data = [{"depth": 1.5, "N60": 5}, {"depth": 3.0, "N60": 8}]
with open("out.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["depth", "N60"])
    writer.writeheader()
    writer.writerows(data)
```

This is the same pattern as `pd.DataFrame(data).to_csv()` in Pandas.

---

## Concept 7: Append Mode

```python
with open("log.txt", "a") as f:    # "a" = add to end
    f.write("14:15 — SPT at 6.0m\n")
```

Perfect for drilling logs, training logs, ongoing data collection.

---

## Concept 8: File Existence Check

```python
import os
if os.path.exists("data.csv"):
    # safe to read
else:
    print("File not found!")
```

---

## Complete Pipeline Built Today

```
raw_field_data.csv  →  [Read → Process → Classify]  →  analysis_results.csv
(from driller)              (Python)                     (for client)
                               ↓
                       summary_report.txt
```

---

## 3 Key Takeaways

1. **Always use `with open(...) as f:`** — auto-closes, prevents data loss.

2. **`csv.DictReader`** is the best CSV reader — rows become dicts, access by name. Remember to convert strings to numbers!

3. **Real workflow: CSV in → Process → CSV out.** This is exactly how ML pipelines work (ETL: Extract-Transform-Load).

---

## How This Connects to ML

| Today | ML Equivalent |
|-------|---------------|
| `csv.DictReader` | `pd.read_csv()` |
| `csv.DictWriter` | `df.to_csv()` |
| Read → process → write | ETL pipeline |
| Append mode | Logging training metrics per epoch |
| `os.path.exists` | Checking for saved model checkpoints |

---

*Day 008 of 100 — We can now read and write real data files!*
