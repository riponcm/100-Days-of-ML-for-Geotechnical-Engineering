"""
Day 008: File I/O — Read & Write CSV, TXT
100 Days of ML for Geotechnical Engineering
Phase: Python Fundamentals

Author: Ripon Chandra Malo
Date: February 23, 2026

Geotechnical Problem: Reading Field Data & Saving Analysis Reports
──────────────────────────────────────────────────────────────────
Until now, all our data was HARDCODED inside the script:
    n_values = [5, 8, 12, 18, ...]

Real projects don't work like this. Real data lives in FILES:
    - borehole_log.csv from the drilling company
    - lab_results.txt from the soils lab
    - spt_data.csv from your database

And your results need to be SAVED to files:
    - analysis_report.csv for the client
    - processed_data.txt for the project archive

File I/O (Input/Output) is the bridge between your Python code
and the outside world. Today we learn to:
  1. READ data from text and CSV files
  2. WRITE results to text and CSV files
  3. Use the 'with' statement for safe file handling
  4. Parse real geotechnical field data from files
"""

import os
import csv

# Create a working directory for our files
os.makedirs("geotech_data", exist_ok=True)


# ══════════════════════════════════════════════════════════════
# PART 1: WRITING TEXT FILES — Save Data to Disk
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 1: WRITING TEXT FILES")
print("=" * 60)

# open() creates or opens a file
# Mode "w" = Write (creates new file, overwrites if exists)
# Mode "r" = Read (default, file must exist)
# Mode "a" = Append (add to end of existing file)

# METHOD 1: open() + close() — works but risky
file = open("geotech_data/field_note.txt", "w")
file.write("Borehole: BH-01\n")
file.write("Location: Salt Lake City, Utah\n")
file.write("Date: 2026-02-23\n")
file.write("Water table: 3.2m\n")
file.close()  # MUST close! Forgetting this can lose data.

print("Wrote field_note.txt (open/close method)")

# METHOD 2: 'with' statement — ALWAYS use this! Auto-closes.
with open("geotech_data/field_note_v2.txt", "w") as file:
    file.write("Borehole: BH-01\n")
    file.write("Location: Salt Lake City, Utah\n")
    file.write("Date: 2026-02-23\n")
    file.write("Water table: 3.2m\n")
# File automatically closed here — even if an error occurs!

print("Wrote field_note_v2.txt (with statement — recommended!)")
print()

# The 'with' statement is like a SAFETY NET:
# - Opens the file
# - Lets you work with it
# - AUTOMATICALLY closes it when done (or if an error happens)
# - ALWAYS use 'with' for file operations!


# ══════════════════════════════════════════════════════════════
# PART 2: READING TEXT FILES — Load Data from Disk
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 2: READING TEXT FILES")
print("=" * 60)

# Read the file we just wrote
# .read() — reads ENTIRE file as one big string
with open("geotech_data/field_note_v2.txt", "r") as file:
    content = file.read()

print("Read entire file with .read():")
print(content)

# .readlines() — reads ALL lines into a LIST
with open("geotech_data/field_note_v2.txt", "r") as file:
    lines = file.readlines()

print(f"Read with .readlines() → list of {len(lines)} lines:")
for i, line in enumerate(lines):
    print(f"  [{i}] '{line.strip()}'")
print()

# .readline() — reads ONE line at a time
with open("geotech_data/field_note_v2.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()

print(f"First line:  '{first_line.strip()}'")
print(f"Second line: '{second_line.strip()}'")
print()

# BEST WAY: Loop through lines (memory efficient)
print("Loop through lines (best for large files):")
with open("geotech_data/field_note_v2.txt", "r") as file:
    for line_num, line in enumerate(file, start=1):
        print(f"  Line {line_num}: {line.strip()}")
print()


# ══════════════════════════════════════════════════════════════
# PART 3: WRITING BOREHOLE DATA TO A TEXT FILE
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 3: WRITING STRUCTURED DATA")
print("=" * 60)

# Write a complete borehole log as a text file
depths =     [1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0]
n_values =   [5, 8, 12, 18, 28, 35, 50, 60]
soil_types = ["Fill", "Silty Sand", "Sand", "Clayey Sand",
              "Sand", "Gravel", "Weathered Rock", "Bedrock"]

with open("geotech_data/bh01_log.txt", "w") as f:
    # Header
    f.write("=" * 55 + "\n")
    f.write("  BOREHOLE LOG — BH-01\n")
    f.write("  Salt Lake City, Utah | WT: 3.2m\n")
    f.write("=" * 55 + "\n")
    f.write(f"  {'#':>2} {'Depth':>6} {'N60':>4} {'Soil':16s} {'Vs':>7}\n")
    f.write("  " + "─" * 40 + "\n")
    
    # Data rows
    for i, (d, n, s) in enumerate(zip(depths, n_values, soil_types), 1):
        Vs = 97 * (n ** 0.314)
        f.write(f"  {i:2d} {d:5.1f}m {n:4d} {s:16s} {Vs:6.1f}\n")
    
    # Summary
    avg_n = sum(n_values) / len(n_values)
    f.write("  " + "─" * 40 + "\n")
    f.write(f"  Avg N: {avg_n:.1f} | Layers: {len(depths)}\n")

print("Wrote bh01_log.txt")

# Verify by reading it back
with open("geotech_data/bh01_log.txt", "r") as f:
    print(f.read())


# ══════════════════════════════════════════════════════════════
# PART 4: WRITING CSV FILES — The Universal Data Format
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 4: WRITING CSV FILES")
print("=" * 60)

# CSV = Comma-Separated Values
# The most common format for exchanging data between tools.
# Excel, Pandas, databases — all read/write CSV.

# METHOD 1: Manual CSV (using string formatting)
with open("geotech_data/bh01_spt.csv", "w") as f:
    # Header row
    f.write("Depth_m,N60,Soil_Type,Vs_ms,Consistency\n")
    
    # Data rows
    for d, n, s in zip(depths, n_values, soil_types):
        Vs = 97 * (n ** 0.314)
        if n < 4: cons = "Very Loose"
        elif n < 10: cons = "Loose"
        elif n < 30: cons = "Medium Dense"
        elif n < 50: cons = "Dense"
        else: cons = "Very Dense"
        
        f.write(f"{d},{n},{s},{Vs:.1f},{cons}\n")

print("Wrote bh01_spt.csv (manual method)")

# METHOD 2: Using csv module (handles commas in data safely)
with open("geotech_data/bh01_spt_v2.csv", "w", newline="") as f:
    writer = csv.writer(f)
    
    # Header
    writer.writerow(["Depth_m", "N60", "Soil_Type", "Vs_ms", "Consistency"])
    
    # Data
    for d, n, s in zip(depths, n_values, soil_types):
        Vs = 97 * (n ** 0.314)
        if n < 10: cons = "Loose"
        elif n < 30: cons = "Medium Dense"
        elif n < 50: cons = "Dense"
        else: cons = "Very Dense"
        writer.writerow([d, n, s, round(Vs, 1), cons])

print("Wrote bh01_spt_v2.csv (csv module — recommended!)")
print()

# Verify
with open("geotech_data/bh01_spt.csv", "r") as f:
    print("CSV contents:")
    print(f.read())


# ══════════════════════════════════════════════════════════════
# PART 5: READING CSV FILES — Load Data for Analysis
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 5: READING CSV FILES")
print("=" * 60)

# METHOD 1: Manual parsing (split by comma)
print("Manual CSV parsing:")
with open("geotech_data/bh01_spt.csv", "r") as f:
    header = f.readline().strip().split(",")
    print(f"  Header: {header}")
    
    data = []
    for line in f:
        parts = line.strip().split(",")
        row = {
            "depth": float(parts[0]),
            "N60": int(parts[1]),
            "soil": parts[2],
            "Vs": float(parts[3]),
            "consistency": parts[4]
        }
        data.append(row)

print(f"  Loaded {len(data)} rows")
print(f"  First row: {data[0]}")
print(f"  Last row:  {data[-1]}")
print()

# METHOD 2: csv.reader (handles edge cases)
print("csv.reader method:")
with open("geotech_data/bh01_spt_v2.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)  # First row is header
    print(f"  Header: {header}")
    
    rows = []
    for row in reader:
        rows.append(row)

print(f"  Loaded {len(rows)} rows")
print(f"  Row 0: {rows[0]}")
print()

# METHOD 3: csv.DictReader — BEST! Each row becomes a dictionary
print("csv.DictReader (best method):")
with open("geotech_data/bh01_spt_v2.csv", "r") as f:
    reader = csv.DictReader(f)
    
    dict_data = []
    for row in reader:
        dict_data.append(row)

print(f"  Loaded {len(dict_data)} rows as dictionaries")
print(f"  Row 0: {dict_data[0]}")
print(f"  Access by name: depth = {dict_data[0]['Depth_m']}, soil = {dict_data[0]['Soil_Type']}")
print()


# ══════════════════════════════════════════════════════════════
# PART 6: APPENDING TO FILES — Adding Data Over Time
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 6: APPENDING TO FILES")
print("=" * 60)

# Mode "a" = Append (add to end, don't overwrite)
# Perfect for logging field data as it arrives

# Create a log file
with open("geotech_data/drilling_log.txt", "w") as f:
    f.write("DRILLING LOG — BH-01\n")
    f.write("=" * 40 + "\n")

# Morning entries
with open("geotech_data/drilling_log.txt", "a") as f:
    f.write("08:00 — Started drilling at 0.0m\n")
    f.write("09:30 — SPT at 1.5m: N=5, Fill\n")
    f.write("10:45 — SPT at 3.0m: N=8, Silty Sand\n")

print("Morning entries appended")

# Afternoon entries (same file, added to end)
with open("geotech_data/drilling_log.txt", "a") as f:
    f.write("13:00 — SPT at 4.5m: N=12, Sand\n")
    f.write("14:15 — SPT at 6.0m: N=18, Clayey Sand\n")
    f.write("16:00 — Water table encountered at 3.2m\n")

print("Afternoon entries appended")
print()

# Read the full log
with open("geotech_data/drilling_log.txt", "r") as f:
    print(f.read())


# ══════════════════════════════════════════════════════════════
# PART 7: FILE EXISTENCE & PATH HANDLING
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 7: FILE CHECKS & PATHS")
print("=" * 60)

# Check if a file exists before reading
filename = "geotech_data/bh01_spt.csv"
print(f"Does '{filename}' exist? {os.path.exists(filename)}")

missing = "geotech_data/bh99_data.csv"
print(f"Does '{missing}' exist? {os.path.exists(missing)}")
print()

# Safe file reading pattern
def safe_read_csv(filepath):
    """Read a CSV file safely — check existence first."""
    if not os.path.exists(filepath):
        print(f"  File not found: {filepath}")
        return None
    
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        return list(reader)

result = safe_read_csv("geotech_data/bh01_spt_v2.csv")
print(f"Found file: {len(result)} rows loaded")

result = safe_read_csv("geotech_data/missing_file.csv")
print()

# List files in directory
print("Files in geotech_data/:")
for filename in sorted(os.listdir("geotech_data")):
    size = os.path.getsize(f"geotech_data/{filename}")
    print(f"  {filename:30s} {size:6d} bytes")
print()


# ══════════════════════════════════════════════════════════════
# PART 8: csv.DictWriter — Write Dicts Directly to CSV
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 8: csv.DictWriter")
print("=" * 60)

# When your data is already a list of dictionaries (Day 006),
# DictWriter writes it directly to CSV — no manual formatting!

processed_layers = [
    {"depth": 1.5, "N60": 5, "soil": "Fill", "Vs": 160.8, "class": "Loose"},
    {"depth": 3.0, "N60": 8, "soil": "Silty Sand", "Vs": 186.4, "class": "Loose"},
    {"depth": 4.5, "N60": 12, "soil": "Sand", "Vs": 211.7, "class": "Med Dense"},
    {"depth": 6.0, "N60": 18, "soil": "Clayey Sand", "Vs": 240.4, "class": "Med Dense"},
    {"depth": 7.5, "N60": 28, "soil": "Sand", "Vs": 276.2, "class": "Med Dense"},
    {"depth": 9.0, "N60": 35, "soil": "Gravel", "Vs": 296.2, "class": "Dense"},
]

fieldnames = ["depth", "N60", "soil", "Vs", "class"]

with open("geotech_data/processed_bh01.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()         # Writes the column names
    writer.writerows(processed_layers)  # Writes ALL rows at once

print("Wrote processed_bh01.csv using DictWriter")

# Verify
with open("geotech_data/processed_bh01.csv", "r") as f:
    print(f.read())


# ══════════════════════════════════════════════════════════════
# PART 9: COMPLETE APPLICATION — Field Data Pipeline
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  COMPLETE: FIELD DATA PIPELINE")
print("=" * 60)

# STEP 1: Create a "field data" CSV (simulating data from drilling company)
with open("geotech_data/raw_field_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["borehole", "depth_m", "N_raw", "soil_description"])
    writer.writerow(["BH-01", "1.5", "5", "Fill (dark brown)"])
    writer.writerow(["BH-01", "3.0", "8", "Silty SAND (SM)"])
    writer.writerow(["BH-01", "4.5", "12", "SAND (SP)"])
    writer.writerow(["BH-01", "6.0", "18", "clayey Sand (SC)"])
    writer.writerow(["BH-01", "7.5", "28", "SAND (SW)"])
    writer.writerow(["BH-01", "9.0", "35", "Gravel (GP)"])
    writer.writerow(["BH-01", "10.5", "50", "weathered ROCK"])
    writer.writerow(["BH-01", "12.0", "60", "BEDROCK"])

print("Step 1: Created raw_field_data.csv")

# STEP 2: Read the raw data
with open("geotech_data/raw_field_data.csv", "r") as f:
    reader = csv.DictReader(f)
    raw_data = list(reader)

print(f"Step 2: Loaded {len(raw_data)} rows from CSV")

# STEP 3: Process each row
wt = 3.2
processed = []

for row in raw_data:
    depth = float(row["depth_m"])
    N_raw = int(row["N_raw"])
    soil = row["soil_description"].strip().title()
    
    N60 = N_raw * (60 / 60)
    Vs = 97 * (N60 ** 0.314)
    
    if N60 < 4: cons = "Very Loose"
    elif N60 < 10: cons = "Loose"
    elif N60 < 30: cons = "Medium Dense"
    elif N60 < 50: cons = "Dense"
    else: cons = "Very Dense"
    
    processed.append({
        "borehole": row["borehole"],
        "depth_m": depth,
        "N60": N60,
        "Vs_ms": round(Vs, 1),
        "soil": soil,
        "consistency": cons,
        "saturated": "Y" if depth > wt else "N",
    })

print(f"Step 3: Processed {len(processed)} layers")

# STEP 4: Write processed results to CSV
out_fields = ["borehole", "depth_m", "N60", "Vs_ms", "soil", "consistency", "saturated"]
with open("geotech_data/analysis_results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=out_fields)
    writer.writeheader()
    writer.writerows(processed)

print("Step 4: Saved analysis_results.csv")

# STEP 5: Write a text summary report
with open("geotech_data/summary_report.txt", "w") as f:
    all_n = [r["N60"] for r in processed]
    all_vs = [r["Vs_ms"] for r in processed]
    
    f.write("=" * 55 + "\n")
    f.write("  SPT ANALYSIS SUMMARY REPORT\n")
    f.write("  BH-01 | Salt Lake City, Utah\n")
    f.write("=" * 55 + "\n\n")
    f.write(f"  Total layers:    {len(processed)}\n")
    f.write(f"  Avg N60:         {sum(all_n)/len(all_n):.1f}\n")
    f.write(f"  Avg Vs:          {sum(all_vs)/len(all_vs):.1f} m/s\n")
    f.write(f"  Weak (N<15):     {len([n for n in all_n if n < 15])}\n")
    f.write(f"  Water table:     {wt}m\n\n")
    
    f.write("  Pipeline: raw_field_data.csv → analysis_results.csv\n")
    f.write("  Generated by: Day 008 File I/O script\n")

print("Step 5: Saved summary_report.txt")
print()

# Show the summary
with open("geotech_data/summary_report.txt", "r") as f:
    print(f.read())

# Show final file listing
print("All generated files:")
for fn in sorted(os.listdir("geotech_data")):
    size = os.path.getsize(f"geotech_data/{fn}")
    print(f"  {fn:30s} {size:6d} bytes")

print("\n" + "=" * 60)
print("  Day 008 Complete!")
print("=" * 60)
