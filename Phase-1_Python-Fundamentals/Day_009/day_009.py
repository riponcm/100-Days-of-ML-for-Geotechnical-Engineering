"""
Day 009: Error Handling — try / except / finally
100 Days of ML for Geotechnical Engineering
Phase: Python Fundamentals

Author: Ripon Chandra Malo
Date: February 24, 2026

Geotechnical Problem: Making Field Data Processing Crash-Proof
──────────────────────────────────────────────────────────────
Real-world geotechnical data is MESSY:
  - A driller types "NR" (No Recovery) instead of a number
  - A CSV file has blank cells where N-values should be
  - A depth column says "3.0m" instead of just "3.0"
  - Someone divides by zero when N60=0 at refusal depth
  - The file you're trying to open doesn't exist

Without error handling, your script CRASHES on the first bad row.
With 1000 rows, you lose ALL results because of ONE bad entry.

Error handling with try/except lets your code:
  1. TRY something that might fail
  2. CATCH the error if it happens
  3. Handle it gracefully (skip row, use default, log warning)
  4. CONTINUE processing the rest of the data

Think of it like FIELD SAFETY PROTOCOLS:
  - You don't stop the entire project because one sample bag tore
  - You LOG the problem, use a backup plan, and KEEP GOING
"""

import csv
import os

os.makedirs("geotech_data", exist_ok=True)


# ══════════════════════════════════════════════════════════════
# PART 1: WHY WE NEED ERROR HANDLING — Seeing Errors First
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 1: COMMON ERRORS IN GEOTECHNICAL DATA")
print("=" * 60)

# Let's see what happens WITHOUT error handling.
# These are all REAL situations in geotechnical data processing.

# ERROR 1: Converting "NR" (No Recovery) to a number
print("Error 1: Bad N-value")
try:
    n_value = int("NR")     # Driller wrote "NR" instead of a number
except ValueError as e:
    print(f"  ValueError: {e}")
    print("  Happens when: N-value is 'NR', '-', or blank\n")

# ERROR 2: Dividing by zero
print("Error 2: Division by zero")
try:
    N60 = 0
    settlement = 150 / N60  # Can't divide by zero!
except ZeroDivisionError as e:
    print(f"  ZeroDivisionError: {e}")
    print("  Happens when: N60=0 at refusal or no-recovery depth\n")

# ERROR 3: File not found
print("Error 3: Missing file")
try:
    with open("missing_borehole.csv", "r") as f:
        data = f.read()
except FileNotFoundError as e:
    print(f"  FileNotFoundError: {e}")
    print("  Happens when: file path is wrong or file was moved\n")

# ERROR 4: Wrong key in dictionary
print("Error 4: Missing dictionary key")
try:
    layer = {"depth": 3.0, "N60": 12}
    soil = layer["soil_type"]  # Key doesn't exist!
except KeyError as e:
    print(f"  KeyError: {e}")
    print("  Happens when: CSV column name doesn't match expected\n")

# ERROR 5: Index out of range
print("Error 5: Index out of range")
try:
    depths = [1.5, 3.0, 4.5]
    value = depths[5]         # Only 3 items!
except IndexError as e:
    print(f"  IndexError: {e}")
    print("  Happens when: accessing row that doesn't exist\n")


# ══════════════════════════════════════════════════════════════
# PART 2: THE try/except BLOCK — Catching Errors
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 2: try / except — THE BASICS")
print("=" * 60)

# Structure:
#   try:
#       code that MIGHT fail
#   except ErrorType:
#       what to do if it fails

# Example: Safely convert a field N-value
def safe_int(value, default=0):
    """Convert to int safely. Return default if conversion fails."""
    try:
        return int(value)
    except ValueError:
        return default

# Test with good and bad data
test_values = ["22", "8", "NR", "", "15", "-", "35"]

print("Converting field N-values safely:")
for val in test_values:
    result = safe_int(val)
    status = "✓" if val.isdigit() else "→ used default"
    print(f"  '{val:3s}' → {result:3d}  {status}")
print()


# ══════════════════════════════════════════════════════════════
# PART 3: CATCHING SPECIFIC ERRORS — Be Precise
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 3: CATCHING SPECIFIC ERRORS")
print("=" * 60)

# Always catch SPECIFIC error types — not just "except:" (too broad)

def process_n_value(raw_value, depth):
    """Process a raw N-value with specific error handling."""
    try:
        n = int(raw_value)
        Vs = 97 * (n ** 0.314)
        ratio = 150 / n          # Might be zero!
        return {"N60": n, "Vs": round(Vs, 1), "ratio": round(ratio, 2)}
    
    except ValueError:
        # "NR", blank, or non-numeric value
        print(f"  ⚠ Depth {depth}m: '{raw_value}' is not a number — skipping")
        return None
    
    except ZeroDivisionError:
        # N-value is 0
        print(f"  ⚠ Depth {depth}m: N=0 — cannot compute ratio")
        return {"N60": 0, "Vs": 0, "ratio": None}

# Test with various field data
test_data = [
    ("22", 1.5), ("NR", 3.0), ("0", 4.5),
    ("18", 6.0), ("", 7.5), ("35", 9.0)
]

print("Processing messy field data:")
results = []
for value, depth in test_data:
    result = process_n_value(value, depth)
    if result:
        results.append(result)
        print(f"  Depth {depth}m: {result}")

print(f"\nProcessed {len(results)} of {len(test_data)} rows successfully")
print()


# ══════════════════════════════════════════════════════════════
# PART 4: THE else CLAUSE — Runs When NO Error Occurs
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 4: try / except / else")
print("=" * 60)

# try:
#     risky code
# except ErrorType:
#     runs if error
# else:
#     runs ONLY if NO error (success path)

def load_borehole_csv(filepath):
    """Load a CSV file with proper error handling."""
    try:
        f = open(filepath, "r")
    except FileNotFoundError:
        print(f"  ✗ File not found: {filepath}")
        return None
    else:
        # This runs ONLY if open() succeeded
        reader = csv.DictReader(f)
        data = list(reader)
        f.close()
        print(f"  ✓ Loaded {len(data)} rows from {filepath}")
        return data

# Create a test file first
with open("geotech_data/test_bh.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["depth", "N60", "soil"])
    writer.writerow([1.5, 5, "Fill"])
    writer.writerow([3.0, 12, "Sand"])

# Test with existing and missing files
load_borehole_csv("geotech_data/test_bh.csv")     # ✓ works
load_borehole_csv("geotech_data/missing.csv")       # ✗ handled
print()


# ══════════════════════════════════════════════════════════════
# PART 5: THE finally CLAUSE — ALWAYS Runs (Cleanup)
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 5: try / except / finally")
print("=" * 60)

# finally: runs NO MATTER WHAT — error or not.
# Use it for CLEANUP: closing files, saving partial results, logging.

# try:
#     risky code
# except ErrorType:
#     handle error
# finally:
#     ALWAYS runs — cleanup, close connections, save state

def process_with_logging(raw_values, log_file="geotech_data/process_log.txt"):
    """Process data and ALWAYS write a log, even if processing fails."""
    processed = []
    errors = []
    
    try:
        for i, val in enumerate(raw_values):
            n = int(val)                    # Might fail!
            Vs = 97 * (n ** 0.314)
            processed.append({"N60": n, "Vs": round(Vs, 1)})
    
    except ValueError as e:
        errors.append(f"Row {i}: ValueError on '{val}' — {e}")
        print(f"  ✗ Error at row {i}: {e}")
    
    finally:
        # This ALWAYS runs — write the log regardless
        with open(log_file, "w") as f:
            f.write(f"Processed: {len(processed)} rows\n")
            f.write(f"Errors: {len(errors)}\n")
            for err in errors:
                f.write(f"  {err}\n")
        print(f"  Log saved to {log_file} (always runs!)")
    
    return processed

# Test: clean data
result = process_with_logging(["5", "12", "22", "35"])
print(f"  Results: {len(result)} rows\n")

# Test: bad data at row 2
result = process_with_logging(["5", "12", "NR", "35"])
print(f"  Results: {len(result)} rows (stopped at error)\n")


# ══════════════════════════════════════════════════════════════
# PART 6: MULTIPLE except BLOCKS — Handle Each Error Differently
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 6: MULTIPLE except BLOCKS")
print("=" * 60)

def safe_layer_analysis(depth_str, n_str, soil, water_table=3.2):
    """
    Analyze one layer with comprehensive error handling.
    Each error type gets its own handling strategy.
    """
    try:
        depth = float(depth_str)
        N60 = int(n_str)
        Vs = 97 * (N60 ** 0.314)
        sigma_v = 18.5 * depth
        settlement_factor = 150 / N60
        
        return {
            "depth": depth, "N60": N60, "Vs": round(Vs, 1),
            "sigma_v": round(sigma_v, 1), "soil": soil,
            "status": "OK"
        }
    
    except ValueError:
        return {"depth": depth_str, "N60": n_str, "soil": soil,
                "status": "BAD_VALUE", "note": f"Cannot convert '{n_str}' to number"}
    
    except ZeroDivisionError:
        return {"depth": float(depth_str), "N60": 0, "soil": soil,
                "Vs": 0, "sigma_v": round(18.5 * float(depth_str), 1),
                "status": "ZERO_N", "note": "N=0, used fallback"}
    
    except TypeError:
        return {"depth": depth_str, "N60": n_str, "soil": soil,
                "status": "TYPE_ERROR", "note": "Unexpected data type"}

# Process messy data
messy_data = [
    ("1.5", "5",  "Fill"),
    ("3.0", "NR", "Sand"),        # ValueError
    ("4.5", "0",  "Clay"),        # ZeroDivisionError
    ("6.0", "18", "Clayey Sand"), # OK
    ("7.5", "",   "Sand"),        # ValueError
    ("9.0", "35", "Gravel"),      # OK
]

print(f"{'Depth':>6} {'N60':>4} {'Soil':14s} {'Status':12s} Note")
print("─" * 55)
for depth, n, soil in messy_data:
    result = safe_layer_analysis(depth, n, soil)
    note = result.get("note", "")
    print(f"{str(depth):>6} {str(n):>4} {soil:14s} {result['status']:12s} {note}")
print()


# ══════════════════════════════════════════════════════════════
# PART 7: RAISING ERRORS — Custom Validation
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 7: RAISING YOUR OWN ERRORS")
print("=" * 60)

# Sometimes YOU want to RAISE an error when data is invalid.
# Use 'raise' to create your own error conditions.

def validate_spt(N60, depth):
    """
    Validate SPT data before analysis.
    Raises ValueError if data doesn't make engineering sense.
    """
    if N60 < 0:
        raise ValueError(f"N60 cannot be negative (got {N60})")
    
    if N60 > 100:
        raise ValueError(f"N60={N60} is unreasonably high (max ~100)")
    
    if depth < 0:
        raise ValueError(f"Depth cannot be negative (got {depth})")
    
    if depth > 100:
        raise ValueError(f"Depth={depth}m seems too deep for SPT (max ~60m)")
    
    return True

# Test validation
test_cases = [
    (22, 6.0, "Normal"),
    (-5, 3.0, "Negative N"),
    (150, 6.0, "Too high N"),
    (22, -2.0, "Negative depth"),
]

for n, d, label in test_cases:
    try:
        validate_spt(n, d)
        print(f"  ✓ N60={n:4d}, depth={d:5.1f}m — Valid")
    except ValueError as e:
        print(f"  ✗ N60={n:4d}, depth={d:5.1f}m — {e}")
print()


# ══════════════════════════════════════════════════════════════
# PART 8: PRACTICAL PATTERN — Skip Bad Rows, Keep Good Ones
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 8: SKIP BAD ROWS, KEEP GOOD ONES")
print("=" * 60)

# THE most important pattern for real data processing:
# Try each row individually. If it fails, LOG it and CONTINUE.

def process_borehole_safe(raw_rows, water_table=3.2):
    """
    Process borehole data, skipping bad rows gracefully.
    Returns: (good_results, error_log)
    """
    good = []
    errors = []
    
    for i, row in enumerate(raw_rows):
        try:
            depth = float(row["depth"])
            N60 = int(row["N60"])
            
            if N60 < 0:
                raise ValueError(f"Negative N60: {N60}")
            
            Vs = 97 * (N60 ** 0.314) if N60 > 0 else 0
            
            if N60 < 4: cons = "Very Loose"
            elif N60 < 10: cons = "Loose"
            elif N60 < 30: cons = "Medium Dense"
            elif N60 < 50: cons = "Dense"
            else: cons = "Very Dense"
            
            good.append({
                "depth": depth, "N60": N60, "Vs": round(Vs, 1),
                "soil": row.get("soil", "Unknown"),
                "consistency": cons,
                "saturated": "Y" if depth > water_table else "N"
            })
        
        except (ValueError, KeyError) as e:
            errors.append({"row": i + 1, "data": row, "error": str(e)})
    
    return good, errors

# Simulate messy CSV data (some rows are bad)
messy_csv = [
    {"depth": "1.5", "N60": "5",  "soil": "Fill"},
    {"depth": "3.0", "N60": "NR", "soil": "Sand"},       # bad!
    {"depth": "4.5", "N60": "12", "soil": "Sand"},
    {"depth": "6.0", "N60": "18", "soil": "Clayey Sand"},
    {"depth": "bad", "N60": "28", "soil": "Sand"},        # bad!
    {"depth": "9.0", "N60": "35", "soil": "Gravel"},
    {"depth": "10.5", "N60": "",  "soil": "Rock"},        # bad!
    {"depth": "12.0", "N60": "60", "soil": "Bedrock"},
]

good, errors = process_borehole_safe(messy_csv)

print(f"Results: {len(good)} good, {len(errors)} errors out of {len(messy_csv)} rows\n")

print("Good rows:")
print(f"  {'Dep':>5} {'N60':>4} {'Soil':14s} {'Class':13s} Sat")
print("  " + "─" * 44)
for r in good:
    print(f"  {r['depth']:4.1f}m {r['N60']:4d} {r['soil']:14s} "
          f"{r['consistency']:13s} {r['saturated']:>3}")

print(f"\nError log ({len(errors)} issues):")
for e in errors:
    print(f"  Row {e['row']}: {e['error']} | data: {e['data']}")
print()


# ══════════════════════════════════════════════════════════════
# PART 9: COMPLETE APPLICATION — Crash-Proof CSV Pipeline
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  COMPLETE: CRASH-PROOF CSV PIPELINE")
print("=" * 60)

# Step 1: Create a messy CSV (simulating real field data)
with open("geotech_data/messy_field_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["borehole", "depth_m", "N_raw", "soil"])
    writer.writerow(["BH-01", "1.5", "5", "Fill"])
    writer.writerow(["BH-01", "3.0", "NR", "Sand"])        # No recovery
    writer.writerow(["BH-01", "4.5", "12", "Sand"])
    writer.writerow(["BH-01", "6.0m", "18", "Clayey Sand"])  # Extra "m"
    writer.writerow(["BH-01", "7.5", "28", "Sand"])
    writer.writerow(["BH-01", "9.0", "", "Gravel"])         # Empty N
    writer.writerow(["BH-01", "10.5", "50", "Rock"])
    writer.writerow(["BH-01", "12.0", "60", "Bedrock"])

print("Step 1: Created messy_field_data.csv")

# Step 2: Read with error handling
try:
    with open("geotech_data/messy_field_data.csv", "r") as f:
        reader = csv.DictReader(f)
        raw_data = list(reader)
    print(f"Step 2: Loaded {len(raw_data)} rows")
except FileNotFoundError:
    print("Step 2: File not found!")
    raw_data = []

# Step 3: Process each row safely
good_results = []
error_log = []

for i, row in enumerate(raw_data, start=1):
    try:
        # Clean depth (remove units like "m")
        depth_clean = row["depth_m"].replace("m", "").strip()
        depth = float(depth_clean)
        
        # Convert N-value
        n_raw = row["N_raw"].strip()
        if n_raw == "" or n_raw.upper() in ["NR", "REF", "-"]:
            raise ValueError(f"Non-numeric N-value: '{row['N_raw']}'")
        
        N60 = int(n_raw)
        Vs = 97 * (N60 ** 0.314) if N60 > 0 else 0
        
        if N60 < 4: cons = "Very Loose"
        elif N60 < 10: cons = "Loose"
        elif N60 < 30: cons = "Medium Dense"
        elif N60 < 50: cons = "Dense"
        else: cons = "Very Dense"
        
        good_results.append({
            "borehole": row["borehole"],
            "depth_m": depth,
            "N60": N60,
            "Vs_ms": round(Vs, 1),
            "soil": row["soil"].strip().title(),
            "consistency": cons,
        })
    
    except (ValueError, KeyError) as e:
        error_log.append(f"Row {i}: {e}")

print(f"Step 3: {len(good_results)} good, {len(error_log)} errors")

# Step 4: Save clean results
if good_results:
    fields = ["borehole", "depth_m", "N60", "Vs_ms", "soil", "consistency"]
    with open("geotech_data/clean_results.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(good_results)
    print("Step 4: Saved clean_results.csv")

# Step 5: Save error log
with open("geotech_data/error_log.txt", "w") as f:
    f.write("ERROR LOG — Messy Field Data Processing\n")
    f.write("=" * 45 + "\n")
    f.write(f"Total rows: {len(raw_data)}\n")
    f.write(f"Successful: {len(good_results)}\n")
    f.write(f"Errors:     {len(error_log)}\n\n")
    for err in error_log:
        f.write(f"  {err}\n")

print("Step 5: Saved error_log.txt")
print()

# Show results
print("Clean results:")
with open("geotech_data/clean_results.csv", "r") as f:
    print(f.read())

print("Error log:")
with open("geotech_data/error_log.txt", "r") as f:
    print(f.read())

print("=" * 60)
print("  Day 009 Complete!")
print("=" * 60)
