"""
Day 005: Lists, Tuples & Sets
100 Days of ML for Geotechnical Engineering
Phase: Python Fundamentals

Author: Ripon Chandra Malo
Date: February 20, 2026

Geotechnical Problem: Managing & Organizing Borehole Datasets
─────────────────────────────────────────────────────────────
Borehole data is fundamentally a COLLECTION of values:
  - A list of depths: [1.5, 3.0, 4.5, 6.0, ...]
  - A list of N-values: [5, 8, 12, 18, ...]
  - A fixed set of sieve sizes: (75.0, 19.0, 4.75, ...)
  - A set of unique soil types encountered: {"Sand", "Clay", "Gravel"}

Each collection type has a specific purpose:
  - LISTS:  Ordered, changeable — data that grows as drilling continues
  - TUPLES: Ordered, fixed — constants that should never be modified
  - SETS:   Unordered, unique — finding distinct soil types, removing duplicates

Today we master all three — the building blocks of every dataset.
"""

# ══════════════════════════════════════════════════════════════
# PART 1: CREATING LISTS — Your First Data Container
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 1: CREATING LISTS")
print("=" * 60)

# A list is an ordered collection inside square brackets []
# Each item can be any type: int, float, str, bool, even another list

# SPT borehole data stored as lists
depths = [1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0]
n_values = [5, 8, 12, 18, 28, 35, 50, 60]
soil_types = ["Fill", "Silty Sand", "Sand", "Clayey Sand",
              "Sand", "Gravel", "Weathered Rock", "Bedrock"]
is_saturated = [False, False, True, True, True, True, True, True]

print(f"Depths:     {depths}")
print(f"N-values:   {n_values}")
print(f"Soil types: {soil_types}")
print(f"Saturated:  {is_saturated}")
print()

# Key properties of lists
print(f"Number of layers: {len(depths)}")
print(f"Type: {type(depths)}")
print()

# Empty list — start collecting data before drilling begins
field_readings = []
print(f"Empty list: {field_readings}, length = {len(field_readings)}")

# List from range
sample_numbers = list(range(1, 9))
print(f"Sample numbers: {sample_numbers}")
print()


# ══════════════════════════════════════════════════════════════
# PART 2: LIST INDEXING & SLICING — Accessing Specific Layers
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 2: LIST INDEXING & SLICING")
print("=" * 60)

# Lists use the same indexing as strings (Day 004)
# Index:    0     1     2     3     4     5     6     7
# Value:    5     8     12    18    28    35    50    60
# Neg:     -8    -7    -6    -5    -4    -3    -2    -1

n_values = [5, 8, 12, 18, 28, 35, 50, 60]

print("INDEXING — Access single items:")
print(f"  n_values[0]  = {n_values[0]}   (first layer — surface)")
print(f"  n_values[3]  = {n_values[3]}   (4th layer, index 3)")
print(f"  n_values[-1] = {n_values[-1]}   (last layer — deepest)")
print(f"  n_values[-2] = {n_values[-2]}   (second to last)")
print()

print("SLICING — Access ranges [start:stop:step]:")
print(f"  n_values[:3]   = {n_values[:3]}       (first 3 layers)")
print(f"  n_values[-3:]  = {n_values[-3:]}     (last 3 layers)")
print(f"  n_values[2:6]  = {n_values[2:6]}   (layers 3-6)")
print(f"  n_values[::2]  = {n_values[::2]}    (every other layer)")
print(f"  n_values[::-1] = {n_values[::-1]}  (reversed — bottom to top)")
print()

# Accessing corresponding data across parallel lists
layer_idx = 3
print(f"Layer {layer_idx + 1} details:")
print(f"  Depth: {depths[layer_idx]}m")
print(f"  N60:   {n_values[layer_idx]}")
print(f"  Soil:  {soil_types[layer_idx]}")
print(f"  Sat:   {is_saturated[layer_idx]}")
print()


# ══════════════════════════════════════════════════════════════
# PART 3: MODIFYING LISTS — Lists are MUTABLE
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 3: MODIFYING LISTS (Mutable!)")
print("=" * 60)

# Unlike strings and tuples, lists CAN be changed after creation.
# This is called being "mutable."

n_copy = [5, 8, 12, 18, 28, 35, 50, 60]

# Change a single value
print(f"Before: {n_copy}")
n_copy[0] = 6  # Corrected first layer reading
print(f"After n_copy[0] = 6: {n_copy}")

# Change a slice
n_copy[1:3] = [10, 14]  # Update layers 2-3
print(f"After n_copy[1:3] = [10, 14]: {n_copy}")
print()

# This is why lists are perfect for field data —
# you can update readings as corrections come in.
print("Lists are MUTABLE → you can change, add, and remove items.")
print("(Strings and tuples are IMMUTABLE → you cannot.)")
print()


# ══════════════════════════════════════════════════════════════
# PART 4: LIST METHODS — Building Data as Field Work Continues
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 4: LIST METHODS")
print("=" * 60)

# Simulate field data arriving one sample at a time
field_n = []
print(f"Start of drilling: {field_n}")

# append() — Add one item at the end
field_n.append(5)     # Layer 1 result arrives
field_n.append(8)     # Layer 2
field_n.append(12)    # Layer 3
print(f"After 3 appends:   {field_n}")

# extend() — Add multiple items at once
field_n.extend([18, 28, 35])  # Afternoon batch arrives
print(f"After extend:      {field_n}")

# insert(index, value) — Add at a specific position
field_n.insert(0, 2)  # Oops, forgot the surface layer!
print(f"After insert at 0: {field_n}")

# pop(index) — Remove and return an item
removed = field_n.pop(0)  # Remove surface (bad reading)
print(f"Popped {removed}:         {field_n}")

# pop() without index removes the last item
last = field_n.pop()
print(f"Popped last ({last}):     {field_n}")

# remove(value) — Remove first occurrence of a value
field_n.append(8)    # Duplicate entry
print(f"With duplicate 8:  {field_n}")
field_n.remove(8)    # Removes the FIRST 8
print(f"After remove(8):   {field_n}")
print()

# Sorting
readings = [28, 5, 18, 12, 35, 8]
print(f"Original:    {readings}")
print(f"sorted():    {sorted(readings)}")      # Returns NEW list
print(f"Original:    {readings}")                # Unchanged!

readings.sort()                                   # Modifies IN PLACE
print(f"After .sort(): {readings}")              # Changed!

readings.sort(reverse=True)
print(f"Descending:  {readings}")
print()

# Useful operations
n_values = [5, 8, 12, 18, 28, 35, 50, 60]
print(f"len():    {len(n_values)} layers")
print(f"min():    {min(n_values)}")
print(f"max():    {max(n_values)}")
print(f"sum():    {sum(n_values)}")
print(f"average:  {sum(n_values)/len(n_values):.1f}")
print(f"count(5): {n_values.count(5)} occurrence(s)")
print(f"index(18):{n_values.index(18)} (position of 18)")
print()


# ══════════════════════════════════════════════════════════════
# PART 5: LIST COMPREHENSION — The Pythonic Shortcut
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 5: LIST COMPREHENSION")
print("=" * 60)

# List comprehension creates a new list by transforming each item.
# It replaces a 4-line for loop with 1 line.

# Traditional loop (Day 003 style):
vs_loop = []
for n in n_values:
    vs_loop.append(97 * (n ** 0.314))

# List comprehension (Day 005 style):
vs_comp = [97 * (n ** 0.314) for n in n_values]

print("Traditional loop vs List Comprehension:")
print(f"  Loop result: {[round(v,1) for v in vs_loop]}")
print(f"  Comp result: {[round(v,1) for v in vs_comp]}")
print(f"  Same? {vs_loop == vs_comp}")
print()

# Syntax:
# [expression FOR variable IN iterable]
# ↑ what to do  ↑ each item  ↑ source data

# More examples
depths = [1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0]

# Overburden pressure: σv = γ × z
sigma_v = [18.5 * d for d in depths]
print(f"σv (kN/m²): {[round(s,1) for s in sigma_v]}")

# Relative density: Dr = 21 × √N60
Dr = [21 * (n ** 0.5) for n in n_values]
print(f"Dr (%):     {[round(d,1) for d in Dr]}")

# Quick labels
labels = ["Weak" if n < 15 else "Strong" for n in n_values]
print(f"Labels:     {labels}")

# Convert all to strings (for CSV output)
n_strings = [str(n) for n in n_values]
print(f"As strings: {n_strings}")
print()


# ══════════════════════════════════════════════════════════════
# PART 6: FILTERED LIST COMPREHENSION — With Conditions
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 6: FILTERED LIST COMPREHENSION")
print("=" * 60)

n_values = [5, 8, 12, 18, 28, 35, 50, 60]
depths =   [1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0]
soils =    ["Fill", "Silty Sand", "Sand", "Clayey Sand",
            "Sand", "Gravel", "Weathered Rock", "Bedrock"]

# Syntax:
# [expression FOR variable IN iterable IF condition]

# Only strong layers (N >= 20)
strong = [n for n in n_values if n >= 20]
print(f"Strong (N>=20):   {strong}")

# Only weak layers
weak = [n for n in n_values if n < 15]
print(f"Weak (N<15):      {weak}")

# Depths below water table
wt = 3.2
sat_depths = [d for d in depths if d > wt]
print(f"Saturated depths: {sat_depths}")

# N-values of sandy layers (using zip from Day 003)
sandy_n = [n for n, s in zip(n_values, soils) if "Sand" in s]
print(f"Sandy layer N:    {sandy_n}")

# Complex filter: saturated + weak + sandy = liquefaction risk
risky = [(d, n, s) for d, n, s in zip(depths, n_values, soils)
         if d > wt and n < 20 and "Sand" in s]
print(f"Risky layers:     {risky}")

# Count with comprehension
weak_count = len([n for n in n_values if n < 15])
print(f"Weak layer count: {weak_count}")
print()


# ══════════════════════════════════════════════════════════════
# PART 7: TUPLES — Immutable Data That Should Never Change
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 7: TUPLES — Immutable Collections")
print("=" * 60)

# A tuple is like a list BUT it CANNOT be changed after creation.
# Created with parentheses () instead of square brackets []

# Borehole coordinates — should NEVER change
bh01_location = (40.7608, -111.8910, 1320.5)  # (lat, lon, elevation)
print(f"BH-01 coordinates: {bh01_location}")
print(f"Type: {type(bh01_location)}")
print()

# Indexing works the same as lists
print(f"Latitude:  {bh01_location[0]}")
print(f"Longitude: {bh01_location[1]}")
print(f"Elevation: {bh01_location[2]}m")
print()

# Unpacking — assign each element to a separate variable
lat, lon, elev = bh01_location
print(f"Unpacked: lat={lat}, lon={lon}, elev={elev}")
print()

# Standard sieve sizes — fixed engineering standard
sieve_sizes_mm = (75.0, 19.0, 4.75, 2.0, 0.425, 0.075)
print(f"Standard sieves: {sieve_sizes_mm}")
print(f"Number of sieves: {len(sieve_sizes_mm)}")
print()

# Atterberg limit classification boundaries — never change
LL_boundary = (30, 50)  # Low plasticity < 30, High > 50
print(f"LL boundaries: {LL_boundary}")
print()

# Tuple of tuples — a read-only data table
borehole_coords = (
    ("BH-01", 40.7608, -111.8910),
    ("BH-02", 40.7615, -111.8895),
    ("BH-03", 40.7602, -111.8920),
)

print("Borehole Coordinates:")
for name, lat, lon in borehole_coords:
    print(f"  {name}: ({lat}, {lon})")
print()

# WHY tuples? They PROTECT data from accidental changes.
# This would cause TypeError:
# bh01_location[0] = 41.0  ← ERROR! Can't modify tuple.
# sieve_sizes_mm.append(0.01)  ← ERROR! No append method.
print("Tuples are IMMUTABLE — they protect constants from changes.")
print("Use them for coordinates, standards, and fixed configurations.")
print()


# ══════════════════════════════════════════════════════════════
# PART 8: LIST vs TUPLE — When to Use Which
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 8: LIST vs TUPLE — Decision Guide")
print("=" * 60)

# LIST: Data that changes, grows, or gets processed
n_values_list = [5, 8, 12]
n_values_list.append(18)    # Can add items!
n_values_list[0] = 6        # Can change items!
print(f"List (mutable):   {n_values_list} — can modify")

# TUPLE: Fixed data, constants, things that shouldn't change
coords = (40.76, -111.89)
# coords[0] = 41.0         # Would cause TypeError!
# coords.append(1320)      # Would cause AttributeError!
print(f"Tuple (immutable): {coords} — cannot modify")
print()

print("Decision Guide:")
print("  Will the data change? → LIST")
print("     SPT readings, field measurements, processed results")
print("  Should the data stay fixed? → TUPLE")
print("     Coordinates, sieve sizes, standard constants")
print("  Returning multiple values from a function? → TUPLE")
print("     return (N60, Vs, consistency)")
print()


# ══════════════════════════════════════════════════════════════
# PART 9: SETS — Unique Values & Set Operations
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 9: SETS — Unique Values Only")
print("=" * 60)

# A set is an UNORDERED collection of UNIQUE items.
# Created with curly braces {} or set()

# Problem: What UNIQUE soil types did we encounter?
soil_log = ["Fill", "Sand", "Clay", "Sand", "Gravel",
            "Sand", "Clay", "Sand", "Gravel", "Bedrock"]

print(f"Full soil log ({len(soil_log)} entries): {soil_log}")

# Convert to set — duplicates automatically removed!
unique_soils = set(soil_log)
print(f"Unique soils ({len(unique_soils)} types):  {unique_soils}")
print()

# Creating sets
sieve_set = {75.0, 19.0, 4.75, 2.0, 0.425, 0.075}
print(f"Sieve set: {sieve_set}")

# Sets ignore duplicates automatically
test = {1, 2, 3, 2, 1, 3, 4}
print(f"{{1,2,3,2,1,3,4}} → {test}")  # Only unique values kept
print()

# Adding and removing
soils_found = {"Sand", "Clay"}
soils_found.add("Gravel")       # Add one item
soils_found.add("Sand")         # Already exists — no effect!
print(f"After add: {soils_found}")

soils_found.discard("Clay")     # Remove (no error if missing)
print(f"After discard: {soils_found}")
print()


# ══════════════════════════════════════════════════════════════
# PART 10: SET OPERATIONS — Comparing Boreholes
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 10: SET OPERATIONS — Comparing Data")
print("=" * 60)

# Soil types found in different boreholes
bh01_soils = {"Fill", "Sand", "Silty Sand", "Clay", "Gravel", "Bedrock"}
bh02_soils = {"Fill", "Sand", "Clay", "Silt", "Weathered Rock"}
bh03_soils = {"Sand", "Gravel", "Cobbles", "Bedrock"}

print(f"BH-01 soils: {bh01_soils}")
print(f"BH-02 soils: {bh02_soils}")
print(f"BH-03 soils: {bh03_soils}")
print()

# UNION (|): All soil types found at the site (combined)
all_soils = bh01_soils | bh02_soils | bh03_soils
print(f"ALL soils at site (union):        {all_soils}")
print(f"  Total unique types: {len(all_soils)}")
print()

# INTERSECTION (&): Soils found in ALL boreholes
common_soils = bh01_soils & bh02_soils & bh03_soils
print(f"Common to ALL boreholes (inter):  {common_soils}")
print()

# DIFFERENCE (-): Soils in BH-01 but NOT in BH-02
only_bh01 = bh01_soils - bh02_soils
print(f"Only in BH-01 (difference):       {only_bh01}")
print()

# SYMMETRIC DIFFERENCE (^): Soils in one OR the other, NOT both
unique_to_either = bh01_soils ^ bh02_soils
print(f"Unique to BH-01 or BH-02 (sym):  {unique_to_either}")
print()

# Membership testing — sets are FAST for "in" checks
all_site_soils = bh01_soils | bh02_soils | bh03_soils
print(f"Is 'Sand' at this site?     {'Sand' in all_site_soils}")
print(f"Is 'Peat' at this site?     {'Peat' in all_site_soils}")
print()


# ══════════════════════════════════════════════════════════════
# PART 11: PRACTICAL SET USES — Removing Duplicates & Validation
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 11: PRACTICAL SET USES")
print("=" * 60)

# Use Case 1: Remove duplicate borehole IDs from a field log
field_log_ids = ["BH-01", "BH-02", "BH-01", "BH-03", "BH-02", "BH-01"]
unique_ids = list(set(field_log_ids))
print(f"All IDs:    {field_log_ids}")
print(f"Unique IDs: {unique_ids}")
print(f"Duplicates removed: {len(field_log_ids) - len(unique_ids)}")
print()

# Use Case 2: Validate soil types against allowed values
allowed_soils = {"Sand", "Silt", "Clay", "Gravel", "Fill", "Bedrock",
                 "Silty Sand", "Clayey Sand", "Sandy Silt", "Weathered Rock"}
entered_soils = {"Sand", "Mud", "Clay", "Muck", "Gravel"}

valid = entered_soils & allowed_soils       # Intersection
invalid = entered_soils - allowed_soils      # Difference
print(f"Entered: {entered_soils}")
print(f"Valid:   {valid}")
print(f"Invalid: {invalid}")
print()

# Use Case 3: Find which depths have been tested
planned_depths = {1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0}
tested_depths = {1.5, 3.0, 4.5, 6.0, 7.5}
remaining = planned_depths - tested_depths
print(f"Planned: {sorted(planned_depths)}")
print(f"Tested:  {sorted(tested_depths)}")
print(f"Remaining: {sorted(remaining)}")
print()


# ══════════════════════════════════════════════════════════════
# PART 12: NESTED LISTS — 2D Data (Like a Spreadsheet)
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 12: NESTED LISTS — 2D Data")
print("=" * 60)

# A list of lists = a table (rows × columns)
# Each inner list is one row (one borehole layer)
borehole = [
    [1.5,  5,  "Fill"],
    [3.0,  8,  "Silty Sand"],
    [4.5,  12, "Sand"],
    [6.0,  18, "Clayey Sand"],
    [7.5,  28, "Sand"],
    [9.0,  35, "Gravel"],
    [10.5, 50, "Weathered Rock"],
    [12.0, 60, "Bedrock"],
]

print("Accessing 2D data:")
print(f"  Row 0 (layer 1):   {borehole[0]}")
print(f"  Row 2 (layer 3):   {borehole[2]}")
print(f"  Row 2, N-value:    {borehole[2][1]}")
print(f"  Last row, soil:    {borehole[-1][2]}")
print()

# Extract columns using list comprehension
all_depths = [row[0] for row in borehole]
all_n = [row[1] for row in borehole]
all_soils = [row[2] for row in borehole]
print(f"All depths:  {all_depths}")
print(f"All N-vals:  {all_n}")
print(f"All soils:   {all_soils}")
print()

# Process 2D data
print("Borehole Table:")
print(f"  {'Depth':>6s}  {'N60':>4s}  {'Soil':16s}  {'Vs':>7s}")
print("  " + "─" * 38)
for row in borehole:
    d, n, s = row    # Unpack each row
    vs = 97 * (n ** 0.314)
    print(f"  {d:5.1f}m  {n:4d}  {s:16s}  {vs:6.1f}")
print()


# ══════════════════════════════════════════════════════════════
# PART 13: COMPLETE APPLICATION — Data Pipeline
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  COMPLETE: BOREHOLE DATA PIPELINE")
print("=" * 60)

# Raw data (parallel lists)
depths =   [1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0]
n_raw =    [5, 8, 12, 18, 28, 35, 50, 60]
soils =    ["Fill", "Silty Sand", "Sand", "Clayey Sand",
            "Sand", "Gravel", "Weathered Rock", "Bedrock"]
wt = 3.2

# Step 1: Compute derived values (list comprehension)
n60 = [n * (60/60) for n in n_raw]
vs = [97 * (n ** 0.314) for n in n60]
sigma_v = [18.5 * d for d in depths]
saturated = [d > wt for d in depths]

# Step 2: Classify (comprehension with function)
def classify(n):
    if n < 4: return "V.Loose"
    elif n < 10: return "Loose"
    elif n < 30: return "Med Dense"
    elif n < 50: return "Dense"
    else: return "V.Dense"

classes = [classify(n) for n in n60]

# Step 3: Filter risky layers
risky_layers = [(d, n, s) for d, n, s in zip(depths, n60, soils)
                if d > wt and n < 20 and "Sand" in s]

# Step 4: Find unique soil types (set)
unique_soils = set(soils)

# Step 5: Statistics (built-in functions on lists)
avg_n = sum(n60) / len(n60)
avg_vs = sum(vs) / len(vs)
weak_count = len([n for n in n60 if n < 15])
sat_count = sum(saturated)  # True = 1, False = 0

# Step 6: Coordinates (tuple — fixed)
site_location = (40.7608, -111.8910, "Salt Lake City, Utah")

# Report
lat, lon, city = site_location
print(f"  Location: {city} ({lat}, {lon})")
print(f"  Unique soils: {unique_soils}")
print("─" * 75)
print(f"  {'#':>2} {'Dep':>5} {'N60':>4} {'Soil':16s} {'Class':9s} {'Vs':>6} {'σv':>6} Sat")
print("─" * 75)

for i, (d, n, s, c, v, sv, st) in enumerate(
    zip(depths, n60, soils, classes, vs, sigma_v, saturated), start=1):
    flag = "Y" if st else "N"
    print(f"  {i:2d} {d:4.1f}m {n:4.0f} {s:16s} {c:9s} {v:5.1f} {sv:5.1f} {flag:>3}")

print("─" * 75)
print(f"  Avg N: {avg_n:.1f} | Avg Vs: {avg_vs:.1f} m/s | Weak: {weak_count} | Sat: {sat_count}")
if risky_layers:
    print(f"  Liquefaction risk: {len(risky_layers)} layer(s)")
    for d, n, s in risky_layers:
        print(f"    → {d}m, N={n:.0f}, {s}")

print("\n" + "=" * 60)
print("  Day 005 Complete!")
print("=" * 60)
