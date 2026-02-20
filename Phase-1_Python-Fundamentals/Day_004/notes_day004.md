# Day 004 | Strings & String Methods

**100 Days of ML for Geotechnical Engineering** | Phase 1: Python Fundamentals
Author: Ripon Chandra Malo | Date: February 19, 2026

---

## Geotechnical Problem We Solved Today

Real geotechnical data arrives as **text** — field logs, CSV files, lab reports. A typical line looks like:

```
"BH-01, Depth: 6.5m, N=22, Soil: Silty SAND (SM), grey-brown"
```

We built a **field log parser** that takes 8 lines of raw text and:
1. Splits each line into parts using `split(",")`
2. Extracts depth and N-values from text using `split("=")` and `replace("m", "")`
3. Standardizes soil names with `.title()`
4. Computes Vs and classifies consistency
5. Generates a formatted report using f-strings
6. Builds CSV output using `join()`

---

## Concept 1: Creating Strings

```python
single = 'BH-01'              # Single quotes
double = "BH-01"              # Double quotes (same thing)
multi = """Line 1              # Triple quotes for multi-line
Line 2
Line 3"""
raw = r"C:\Users\data"        # Raw string (ignores \)
```

Special characters: `\n` = new line, `\t` = tab, `\\` = literal backslash

---

## Concept 2: Indexing & Slicing

Strings are sequences — each character has a position.

```
String:  B  H  -  0  1  -  S  P  T
Index:   0  1  2  3  4  5  6  7  8
Neg:    -9 -8 -7 -6 -5 -4 -3 -2 -1
```

| Syntax | Result | Meaning |
|--------|--------|---------|
| `s[0]` | `"B"` | First character |
| `s[-1]` | `"T"` | Last character |
| `s[:5]` | `"BH-01"` | First 5 characters |
| `s[6:]` | `"SPT"` | From index 6 to end |
| `s[3:5]` | `"01"` | Characters at index 3,4 |
| `s[::-1]` | `"TPS-10-HB"` | Reversed |

**Important:** Strings are **immutable** — you cannot change individual characters. You create a new string instead.

---

## Concept 3: Concatenation & Repetition

```python
"BH" + "-" + "01"     # → "BH-01"  (concatenation with +)
"─" * 40               # → 40 dashes (repetition with *)
```

**Common mistake:** `"Depth: " + 6.5` → TypeError! Fix with `str(6.5)` or use f-strings.

---

## Concept 4: f-Strings (Formatted String Literals)

The modern way to embed variables and format text.

```python
f"Borehole {bh_id} at {depth}m: N60={N60:.1f}"
```

### Format Specifiers

| Format | Meaning | Example | Output |
|--------|---------|---------|--------|
| `{x:.1f}` | 1 decimal | `f"{3.14:.1f}"` | `"3.1"` |
| `{x:.2f}` | 2 decimals | `f"{3.14:.2f}"` | `"3.14"` |
| `{x:8.1f}` | Right-align, width 8 | `f"{3.1:8.1f}"` | `"     3.1"` |
| `{x:.1%}` | Percentage | `f"{0.65:.1%}"` | `"65.0%"` |
| `{x:.2e}` | Scientific | `f"{120000:.2e}"` | `"1.20e+05"` |
| `{s:<15}` | Left-align | Fills 15 chars | `"Sand           "` |
| `{s:>15}` | Right-align | Fills 15 chars | `"           Sand"` |

---

## Concept 5: Case Methods

Standardize inconsistent field data capitalization.

| Method | Input → Output |
|--------|---------------|
| `.upper()` | `"sand"` → `"SAND"` |
| `.lower()` | `"SAND"` → `"sand"` |
| `.title()` | `"silty SAND"` → `"Silty Sand"` |
| `.capitalize()` | `"silty SAND"` → `"Silty sand"` |

**Key use:** Always `.lower()` or `.title()` before comparing strings:

```python
# Without: "Clay" == "CLAY" → False!
# With:    "Clay".lower() == "CLAY".lower() → True!
```

---

## Concept 6: strip(), replace(), find()

| Method | Purpose | Example |
|--------|---------|--------|
| `.strip()` | Remove whitespace from both ends | `"  BH-01  "` → `"BH-01"` |
| `.replace(old, new)` | Substitute text | `"6.5m".replace("m","")` → `"6.5"` |
| `.find(text)` | Position of text (-1 if not found) | `"N=22".find("=")` → `1` |
| `in` | Check if text exists | `"Sand" in "Silty Sand"` → `True` |

---

## Concept 7: split() & join() — THE Most Important Methods

**split()** — Break a string into a list:

```python
"BH-01,6.5,22,Sand".split(",")  →  ["BH-01", "6.5", "22", "Sand"]
"N=22".split("=")               →  ["N", "22"]
```

**join()** — Combine a list into a string:

```python
",".join(["BH-01", "6.5", "22"])  →  "BH-01,6.5,22"
"\n".join(["Line 1", "Line 2"])   →  "Line 1\nLine 2"
```

### The Data Cleaning Pattern

```python
messy = "  BH-01 ,  6.5  ,  22  "
clean = [p.strip() for p in messy.split(",")]  # Split + Strip
output = ", ".join(clean)                        # Rejoin clean
```

---

## Concept 8: Checking Methods

| Method | Checks | `"22"` | `"6.5"` | `"Sand"` |
|--------|--------|--------|---------|----------|
| `.isdigit()` | All digits? | True | False | False |
| `.isalpha()` | All letters? | False | False | True |
| `.startswith("BH")` | Starts with? | — | — | — |
| `.endswith(".csv")` | Ends with? | — | — | — |

---

## Complete Application: What We Built

A field log parser that converts raw text into a structured report:

```
Input:  "BH-01, 6.0m, N=18, clayey Sand (SC), stiff, grey, wet"
                    ↓ split + strip + replace + title + int/float
Output: depth=6.0 | N60=18 | Soil="Clayey Sand (Sc)" | Vs=240.4 | Med Dense
```

---

## 3 Key Takeaways

1. **split() and join()** are the workhorses of text data processing. `split` breaks text into lists (parsing), `join` builds text from lists (formatting). Master these two and you can parse any text file.

2. **f-strings** (`f"N60 = {N60:.1f}"`) are the modern way to format output. The format specifiers (`.1f`, `>8`, etc.) give you precise control over how numbers and text appear in reports.

3. **The pattern split → strip → process → join** appears in every data pipeline. Raw field text → split into parts → clean each part → convert to numbers → calculate → format output. This is exactly what Pandas `.str` methods do to entire columns at once.

---

## How This Connects to ML

| Today | ML Equivalent |
|-------|---------------|
| Parsing text | NLP preprocessing, tokenization |
| `.lower()` standardization | Text normalization before ML |
| `.split()` | Tokenization in NLP models |
| Extracting numbers | Feature extraction from raw data |
| `.replace()` cleaning | `df['col'].str.replace()` in Pandas |
| `in` for filtering | `df[df['soil'].str.contains('Sand')]` |
| CSV generation | Exporting model predictions |

---

*Day 004 of 100 — We can now parse raw field data into clean numbers!*
