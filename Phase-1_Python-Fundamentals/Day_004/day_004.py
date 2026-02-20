"""
Day 004: Strings & String Methods
100 Days of ML for Geotechnical Engineering
Phase: Python Fundamentals

Author: Ripon Chandra Malo
Date: February 19, 2026

Geotechnical Problem: Parsing & Formatting Borehole Log Text Data
─────────────────────────────────────────────────────────────────
Real geotechnical data doesn't arrive as clean numbers. It comes
as TEXT in field logs, CSV files, lab reports, and PDF extractions.

Example from a digital field tablet:
   "BH-01, Depth: 6.5m, N=22, Soil: Silty SAND (SM), grey-brown"

Before we can do ANY calculation, we need to:
  1. Extract the numbers from this text
  2. Clean up inconsistent formatting
  3. Split the string into useful pieces
  4. Build formatted reports from our results

Today we master Python strings — the bridge between raw field
data and the clean numbers our calculations need.
"""

# ══════════════════════════════════════════════════════════════
# PART 1: CREATING STRINGS — The Basics
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 1: CREATING STRINGS")
print("=" * 60)

# Strings are text wrapped in quotes — single or double both work
borehole_id = 'BH-01'
project_name = "Highway Bridge Foundation"
soil_type = "Silty SAND"

print(f"Borehole:  {borehole_id}")
print(f"Project:   {project_name}")
print(f"Soil type: {soil_type}")
print()

# Triple quotes for multi-line strings (great for reports)
field_note = """Borehole: BH-01
Location: Salt Lake City, Utah
Date: 2026-02-19
Driller: ABC Drilling Co.
Water table encountered at 3.2m"""

print("Field Note (multi-line string):")
print(field_note)
print()

# String with special characters
# \n = new line, \t = tab
log_entry = "Layer 1:\tFill\t\tN=5\nLayer 2:\tSilty Sand\tN=8"
print("Formatted with \\n and \\t:")
print(log_entry)
print()

# Raw string (ignores escape characters) — useful for file paths
file_path = r"C:\Users\new\Documents\borehole_data.csv"
print(f"Raw string path: {file_path}")
print()


# ══════════════════════════════════════════════════════════════
# PART 2: STRING INDEXING & SLICING — Accessing Characters
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 2: STRING INDEXING & SLICING")
print("=" * 60)

# Strings are sequences — each character has an index
# Index:    0  1  2  3  4  5  6  7  8  9  10 11 12
sample_id = "BH-01-SPT-06"

print(f"String: '{sample_id}'")
print(f"Length: {len(sample_id)} characters")
print()

# Positive indexing (from left, starts at 0)
print("Positive indexing:")
print(f"  [0]  = '{sample_id[0]}'   (first character)")
print(f"  [1]  = '{sample_id[1]}'")
print(f"  [5]  = '{sample_id[5]}'")
print(f"  [11] = '{sample_id[11]}'  (last character)")
print()

# Negative indexing (from right, starts at -1)
print("Negative indexing:")
print(f"  [-1] = '{sample_id[-1]}'  (last character)")
print(f"  [-2] = '{sample_id[-2]}'  (second to last)")
print(f"  [-5] = '{sample_id[-5]}'")
print()

# Slicing [start:stop] — stop is NOT included
print("Slicing:")
print(f"  [:2]   = '{sample_id[:2]}'          (first 2: borehole prefix)")
print(f"  [:5]   = '{sample_id[:5]}'        (first 5: borehole ID)")
print(f"  [6:9]  = '{sample_id[6:9]}'         (chars 6,7,8: test type)")
print(f"  [-2:]  = '{sample_id[-2:]}'          (last 2: sample number)")
print(f"  [::2]  = '{sample_id[::2]}'     (every 2nd character)")
print(f"  [::-1] = '{sample_id[::-1]}'  (reversed)")
print()

# IMPORTANT: Strings are IMMUTABLE (like tuples)
# sample_id[0] = "C"  # This would cause TypeError!
print("Strings are IMMUTABLE — you cannot change individual characters.")
print("You create a NEW string instead (we'll see how below).")
print()


# ══════════════════════════════════════════════════════════════
# PART 3: STRING CONCATENATION & REPETITION — Building Strings
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 3: CONCATENATION & REPETITION")
print("=" * 60)

# Concatenation with +
prefix = "BH"
number = "03"
borehole = prefix + "-" + number
print(f"Concatenation: '{prefix}' + '-' + '{number}' = '{borehole}'")

# Repetition with *
separator = "─" * 40
print(f"Repetition: '─' * 40 = {separator}")

# Building a header
title = "SPT BOREHOLE LOG"
border = "=" * 30
header = border + "\n  " + title + "\n" + border
print(f"\n{header}")
print()

# Common mistake: can't add string + number directly
depth = 6.5
# wrong: "Depth: " + depth      → TypeError!
# right: "Depth: " + str(depth)  → works!
print("Depth: " + str(depth) + "m")
print(f"Better way: Depth: {depth}m")  # f-string (covered next)
print()


# ══════════════════════════════════════════════════════════════
# PART 4: f-STRINGS — The Modern Way to Format Text
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 4: f-STRINGS (Formatted String Literals)")
print("=" * 60)

# f-strings let you embed variables and expressions inside strings
# Just put f before the quotes and use {curly braces}

bh_id = "BH-01"
depth = 6.5
N60 = 22.0
soil = "Silty Sand"
Vs = 97 * (N60 ** 0.314)

# Basic embedding
print(f"Borehole {bh_id} at {depth}m: N60={N60}, {soil}")
print()

# Number formatting inside f-strings
print("Number formatting:")
print(f"  No format:  Vs = {Vs}")
print(f"  1 decimal:  Vs = {Vs:.1f} m/s")
print(f"  2 decimals: Vs = {Vs:.2f} m/s")
print(f"  Integer:    Vs = {Vs:.0f} m/s")
print(f"  Width 8:    Vs = {Vs:8.1f} m/s")  # right-align in 8 chars
print(f"  Percentage: Dr = {0.65:.1%}")       # 0.65 → 65.0%
print(f"  Scientific: σ  = {120500:.2e} Pa")  # 1.21e+05
print()

# Alignment and padding (great for tables)
print("Alignment in f-strings:")
print(f"  {'Left':<15} | done with <")
print(f"  {'Center':^15} | done with ^")
print(f"  {'Right':>15} | done with >")
print()

# Using expressions inside f-strings
print("Expressions inside f-strings:")
print(f"  N60² = {N60**2:.1f}")
print(f"  Is saturated? {depth > 3.2}")
print(f"  Classification: {'Dense' if N60 >= 30 else 'Not Dense'}")
print()

# Building a formatted table row
print("Formatted table row:")
print(f"  {'Depth':>6s}  {'N60':>5s}  {'Soil':15s}  {'Vs (m/s)':>8s}")
print(f"  {'─'*6}  {'─'*5}  {'─'*15}  {'─'*8}")
print(f"  {depth:5.1f}m  {N60:5.1f}  {soil:15s}  {Vs:8.1f}")
print()


# ══════════════════════════════════════════════════════════════
# PART 5: CASE METHODS — Cleaning Inconsistent Field Data
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 5: CASE METHODS")
print("=" * 60)

# Field data often has inconsistent capitalization:
# "silty SAND", "Silty sand", "SILTY SAND", "silty Sand"
# We need to standardize it!

raw_soil = "silty SAND (sm), grey-Brown, wet"

print(f"Original:    '{raw_soil}'")
print(f".upper():    '{raw_soil.upper()}'")
print(f".lower():    '{raw_soil.lower()}'")
print(f".title():    '{raw_soil.title()}'")
print(f".capitalize():'{raw_soil.capitalize()}'")
print(f".swapcase(): '{raw_soil.swapcase()}'")
print()

# Practical use: standardize before comparing
user_input1 = "Clay"
user_input2 = "CLAY"
user_input3 = "clay"

# Without .lower(), these are all different!
print(f"'Clay' == 'CLAY'?  {user_input1 == user_input2}")  # False!
print(f"After .lower():    {user_input1.lower() == user_input2.lower()}")  # True!
print()

# Standardize soil descriptions
field_entries = ["silty SAND", "Silty sand", "SILTY SAND", "silty Sand"]
standardized = [s.title() for s in field_entries]
print(f"Field entries:  {field_entries}")
print(f"Standardized:   {standardized}")
print()


# ══════════════════════════════════════════════════════════════
# PART 6: STRIP, REPLACE, FIND — Cleaning & Searching
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 6: STRIP, REPLACE, FIND")
print("=" * 60)

# strip() — Remove whitespace (very common in CSV/text file data)
messy = "   BH-01, Depth: 6.5m   \n"
print(f"Original:  '{messy}'")
print(f".strip():  '{messy.strip()}'")
print(f".lstrip(): '{messy.lstrip()}'")  # left only
print(f".rstrip(): '{messy.rstrip()}'")  # right only
print()

# replace() — Substitute text
description = "N-value = 22 blows/300mm"
clean = description.replace("blows/300mm", "").replace("N-value = ", "")
print(f"Original: '{description}'")
print(f"Cleaned:  '{clean.strip()}'")
print()

# Replace units
depth_str = "6.5 ft"
depth_metric = depth_str.replace("ft", "m").replace("6.5", str(6.5 * 0.3048))
print(f"Imperial: {depth_str}")
print(f"Metric:   {depth_metric}")
print()

# find() — Locate text within a string
log_line = "BH-01, Depth: 6.5m, N=22, Soil: Silty Sand"

pos_depth = log_line.find("Depth:")
pos_n = log_line.find("N=")
pos_soil = log_line.find("Soil:")
print(f"Log: '{log_line}'")
print(f"  'Depth:' found at position {pos_depth}")
print(f"  'N=' found at position {pos_n}")
print(f"  'Soil:' found at position {pos_soil}")
print(f"  'Clay' found at position {log_line.find('Clay')}")  # -1 = not found
print()

# in operator — Check if text exists
print(f"  'Sand' in log?  {'Sand' in log_line}")
print(f"  'Clay' in log?  {'Clay' in log_line}")
print()


# ══════════════════════════════════════════════════════════════
# PART 7: SPLIT & JOIN — The Most Powerful String Tools
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 7: SPLIT & JOIN")
print("=" * 60)

# split() — Break a string into a LIST of parts
# This is THE most important string method for data processing

log_line = "BH-01, Depth: 6.5m, N=22, Soil: Silty Sand"

# Split by comma
parts = log_line.split(",")
print(f"Original: '{log_line}'")
print(f"Split by ',': {parts}")
print(f"  Part 0: '{parts[0].strip()}'")
print(f"  Part 1: '{parts[1].strip()}'")
print(f"  Part 2: '{parts[2].strip()}'")
print(f"  Part 3: '{parts[3].strip()}'")
print()

# Split by different delimiters
sample_id = "BH-01-SPT-06"
id_parts = sample_id.split("-")
print(f"'{sample_id}'.split('-') = {id_parts}")
print(f"  Borehole prefix: {id_parts[0]}")
print(f"  Borehole number: {id_parts[1]}")
print(f"  Test type:       {id_parts[2]}")
print(f"  Sample number:   {id_parts[3]}")
print()

# Split to extract numbers
depth_text = "Depth: 6.5m"
depth_value = float(depth_text.split(":")[1].strip().replace("m", ""))
print(f"Text: '{depth_text}' → Extracted number: {depth_value}")

n_text = "N=22"
n_value = int(n_text.split("=")[1])
print(f"Text: '{n_text}' → Extracted number: {n_value}")
print()

# join() — The OPPOSITE of split: combine a list into a string
soil_words = ["Silty", "Sand", "(SM)"]
combined = " ".join(soil_words)
print(f"Join with space:  {soil_words} → '{combined}'")

csv_row = ",".join(["BH-01", "6.5", "22", "Sand"])
print(f"Join with comma:  → '{csv_row}'")

path = "/".join(["data", "boreholes", "BH-01", "spt_log.csv"])
print(f"Join with slash:  → '{path}'")
print()

# Split then rejoin (common data cleaning pattern)
messy_text = "BH-01   ,   6.5  ,  22  ,  Sand"
clean_parts = [part.strip() for part in messy_text.split(",")]
clean_csv = ", ".join(clean_parts)
print(f"Messy: '{messy_text}'")
print(f"Clean: '{clean_csv}'")
print()


# ══════════════════════════════════════════════════════════════
# PART 8: STRING CHECKING METHODS — Validation
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 8: STRING CHECKING METHODS")
print("=" * 60)

# These methods return True/False — great for data validation

test_values = ["22", "6.5", "Sand", "BH-01", "  ", ""]

for val in test_values:
    print(f"  '{val:6s}' → isdigit:{str(val.isdigit()):5s}  "
          f"isalpha:{str(val.isalpha()):5s}  "
          f"isalnum:{str(val.isalnum()):5s}  "
          f"isspace:{str(val.isspace()):5s}")
print()

# Practical: Validate field data
def validate_n_value(text):
    """Check if a string is a valid N-value (positive integer)."""
    clean = text.strip()
    if clean.isdigit():
        n = int(clean)
        if 0 <= n <= 100:
            return True, n
        return False, f"N={n} out of range (0-100)"
    return False, f"'{clean}' is not a number"

# Test validation
test_inputs = ["22", "abc", "150", "  8  ", ""]
print("N-value validation:")
for t in test_inputs:
    valid, result = validate_n_value(t)
    status = f"✓ N={result}" if valid else f"✗ {result}"
    print(f"  Input '{t}' → {status}")
print()

# startswith / endswith — Check prefixes and suffixes
files = ["BH-01_spt.csv", "BH-02_lab.pdf", "BH-03_spt.csv", "report.docx"]
csv_files = [f for f in files if f.endswith(".csv")]
bh_files = [f for f in files if f.startswith("BH")]
print(f"All files:  {files}")
print(f"CSV files:  {csv_files}")
print(f"BH files:   {bh_files}")
print()


# ══════════════════════════════════════════════════════════════
# PART 9: COMPLETE APPLICATION — Parse a Field Log & Build Report
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  COMPLETE APPLICATION: FIELD LOG PARSER")
print("=" * 60)

# Raw field data — exactly as it arrives from a digital tablet
raw_field_log = """
BH-01, 1.5m, N=5, Fill (loose, dark brown), dry
BH-01, 3.0m, N=8, Silty SAND (SM), grey-brown, dry
BH-01, 4.5m, N=12, SAND (SP), medium dense, tan, moist
BH-01, 6.0m, N=18, clayey Sand (SC), stiff, grey, wet
BH-01, 7.5m, N=28, SAND (SW), dense, brown, saturated
BH-01, 9.0m, N=35, Gravel (GP), dense, grey, saturated
BH-01, 10.5m, N=50, weathered ROCK, very dense, grey
BH-01, 12.0m, N=60, BEDROCK (refusal), grey
"""

print("Raw field log:")
print(raw_field_log.strip())
print()

# Parse the log using string methods
print("=" * 75)
print("  PARSED BOREHOLE REPORT — BH-01")
print("  Salt Lake City, Utah | Water Table: 3.2m")
print("=" * 75)
print(f"  {'#':>2}  {'Depth':>6}  {'N60':>4}  {'Soil':22s}  {'Vs':>7}  {'Class':13s}")
print("  " + "─" * 68)

wt = 3.2
parsed_data = []

for line in raw_field_log.strip().split("\n"):
    # Split by comma
    parts = [p.strip() for p in line.split(",")]
    
    # Extract borehole ID
    bh_id = parts[0].strip()                           # "BH-01"
    
    # Extract depth (remove 'm')
    depth = float(parts[1].strip().replace("m", ""))    # "3.0m" → 3.0
    
    # Extract N-value (split by '=')
    N60 = int(parts[2].strip().split("=")[1])           # "N=8" → 8
    
    # Extract soil description (title case for consistency)
    soil_raw = parts[3].strip()                         # "Silty SAND (SM)"
    
    # Standardize: extract main soil type
    soil_clean = soil_raw.title()
    
    # Calculate Vs
    Vs = 97 * (N60 ** 0.314)
    
    # Classify
    if N60 < 4:
        cons = "Very Loose"
    elif N60 < 10:
        cons = "Loose"
    elif N60 < 30:
        cons = "Medium Dense"
    elif N60 < 50:
        cons = "Dense"
    else:
        cons = "Very Dense"
    
    # Store parsed data
    layer_num = len(parsed_data) + 1
    parsed_data.append({
        "depth": depth, "N60": N60, "soil": soil_clean,
        "Vs": Vs, "consistency": cons
    })
    
    print(f"  {layer_num:2d}  {depth:5.1f}m  {N60:4d}  {soil_clean:22s}  {Vs:6.1f}  {cons}")

print("  " + "─" * 68)

# Summary statistics using parsed data
all_n = [d["N60"] for d in parsed_data]
all_vs = [d["Vs"] for d in parsed_data]
avg_vs = sum(all_vs) / len(all_vs)
weak_count = len([n for n in all_n if n < 15])

print(f"  Layers: {len(parsed_data)} | Avg N: {sum(all_n)/len(all_n):.1f} | Avg Vs: {avg_vs:.1f} m/s")
print(f"  Weak layers (N<15): {weak_count} | N range: {min(all_n)} — {max(all_n)}")

# Generate CSV output string
print(f"\n  Generated CSV output:")
csv_header = "Depth_m,N60,Soil,Vs_ms,Consistency"
print(f"  {csv_header}")
for d in parsed_data[:3]:
    csv_row = f"  {d['depth']},{d['N60']},{d['soil']},{d['Vs']:.1f},{d['consistency']}"
    print(csv_row)
print(f"  ... ({len(parsed_data)} rows total)")

print("\n" + "=" * 60)
print("  Day 004 Complete!")
print("=" * 60)
