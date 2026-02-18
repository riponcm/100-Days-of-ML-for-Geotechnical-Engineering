"""
Day 003: Loops — for, while, enumerate, zip
100 Days of ML for Geotechnical Engineering
Phase: Python Fundamentals

Author: Ripon Chandra Malo
Date: February 18, 2026

Geotechnical Problem: Processing Multi-Layer SPT Borehole Data
───────────────────────────────────────────────────────────────
We have SPT data from BH-01 with 8 layers. Instead of writing
the same calculation 8 times (once per layer), loops let us
write it ONCE and repeat automatically. This is the foundation
of processing any dataset — whether 8 rows or 8 million.
"""

# ══════════════════════════════════════════════════════════════
# PART 1: BASIC for LOOP — Iterating Through Borehole Layers
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 1: BASIC for LOOP")
print("=" * 60)

# SPT N-values from 8 depth intervals in BH-01
n_values = [5, 8, 12, 18, 28, 35, 50, 60]

print("SPT N-values from BH-01:")
for n in n_values:
    print(f"  N = {n}")

print()

# Classify each N-value using loop + conditional (Day 002 + Day 003)
print("Soil Consistency for Each Layer:")
for n in n_values:
    if n < 4:
        cons = "Very Loose"
    elif n < 10:
        cons = "Loose"
    elif n < 30:
        cons = "Medium Dense"
    elif n < 50:
        cons = "Dense"
    else:
        cons = "Very Dense"
    print(f"  N = {n:3d} → {cons}")

print()

# ══════════════════════════════════════════════════════════════
# PART 2: for WITH range() — Generating Depth Intervals
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 2: for WITH range()")
print("=" * 60)

# Generate depths: 1.5m to 12.0m at 1.5m intervals
print("SPT sampling depths (1.5m intervals):")
for i in range(8):
    depth = 1.5 * (i + 1)
    print(f"  Sample {i+1}: {depth:.1f} m")

print()

# range(start, stop, step)
print("Even-numbered layers only:")
for i in range(0, 8, 2):
    print(f"  Layer index {i}: N = {n_values[i]}")

print()

# Counting layers with N > 20
strong_layers = 0
for n in n_values:
    if n > 20:
        strong_layers += 1
print(f"Layers with N > 20: {strong_layers} out of {len(n_values)}")

print()

# ══════════════════════════════════════════════════════════════
# PART 3: while LOOP — Drilling Until Refusal
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 3: while LOOP — Drilling Until Refusal")
print("=" * 60)

# Simulate drilling: keep going until we hit N >= 50 (refusal)
# or reach maximum depth of 30m
current_depth = 0.0
increment = 1.5
max_depth = 30.0
layer = 0

# Simulated N-values at each depth (imagine these come from field)
simulated_n = [3, 5, 8, 12, 18, 22, 28, 35, 42, 48, 50]

print("Drilling log (stop at refusal or max depth):")
print(f"  {'Depth':>8s}  {'N-value':>7s}  {'Action'}")
print("  " + "─" * 40)

while current_depth < max_depth:
    current_depth += increment
    
    if layer < len(simulated_n):
        n = simulated_n[layer]
    else:
        n = 50  # assume refusal if we run out of data
    
    if n >= 50:
        print(f"  {current_depth:7.1f}m  {n:>7d}  ← REFUSAL! Stop drilling.")
        break
    else:
        print(f"  {current_depth:7.1f}m  {n:>7d}  Continue drilling...")
    
    layer += 1

print(f"\nFinal depth reached: {current_depth:.1f} m")
print(f"Total layers sampled: {layer + 1}")

print()

# ══════════════════════════════════════════════════════════════
# PART 4: enumerate() — Track Index AND Value Together
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 4: enumerate() — Index + Value")
print("=" * 60)

soil_descriptions = [
    "Fill (loose, dark brown)",
    "Silty Sand (SM, grey-brown)",
    "Sand (SP, medium dense, tan)",
    "Clayey Sand (SC, stiff, grey)",
    "Sand (SW, dense, brown)",
    "Dense Gravel (GP, grey)",
    "Weathered Sandstone",
    "Bedrock (refusal)"
]

print("Borehole Log — Soil Descriptions:")
print(f"  {'Layer':>5s}  {'Depth':>6s}  {'Description'}")
print("  " + "─" * 50)

for index, description in enumerate(soil_descriptions):
    depth = 1.5 * (index + 1)
    print(f"  {index+1:5d}  {depth:5.1f}m  {description}")

print()

# Using enumerate with start parameter
print("Numbered from 1 (using start=1):")
for num, desc in enumerate(soil_descriptions, start=1):
    print(f"  Layer {num}: {desc}")

print()

# ══════════════════════════════════════════════════════════════
# PART 5: zip() — Pairing Parallel Data
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 5: zip() — Combining Parallel Data")
print("=" * 60)

# In geotechnical work, data often comes in separate lists:
depths =      [1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0]
n_values =    [5,   8,   12,  18,  28,  35,  50,   60]
soil_types =  ["Fill", "Silty Sand", "Sand", "Clayey Sand",
               "Sand", "Gravel", "Weathered Rock", "Bedrock"]

print("Combined Borehole Log (zip of 3 lists):")
print(f"  {'Depth':>6s}  {'N60':>4s}  {'Soil Type'}")
print("  " + "─" * 40)

for d, n, s in zip(depths, n_values, soil_types):
    print(f"  {d:5.1f}m  {n:4d}  {s}")

print()

# zip + enumerate — the ultimate combo
print("With layer numbers (enumerate + zip):")
for i, (d, n, s) in enumerate(zip(depths, n_values, soil_types), start=1):
    print(f"  Layer {i}: {d:.1f}m | N={n:3d} | {s}")

print()

# ══════════════════════════════════════════════════════════════
# PART 6: LOOP CONTROL — break, continue, pass
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 6: LOOP CONTROL — break, continue, pass")
print("=" * 60)

# break — stop when we find the first suitable bearing layer
print("Finding first suitable bearing layer (N >= 15):")
for d, n, s in zip(depths, n_values, soil_types):
    if n >= 15:
        print(f"  FOUND at {d:.1f}m: N={n}, {s}")
        print(f"  → Recommend foundation at this depth")
        break
    else:
        print(f"  {d:.1f}m: N={n} — too weak, skip")

print()

# continue — skip non-sandy layers for liquefaction check
print("Liquefaction check (skip non-sandy layers):")
wt = 3.2
for d, n, s in zip(depths, n_values, soil_types):
    if "Sand" not in s:
        continue  # skip this layer, go to next
    if d > wt and n < 20:
        print(f"  {d:.1f}m | N={n} | {s} → LIQUEFIABLE")
    else:
        print(f"  {d:.1f}m | N={n} | {s} → OK")

print()

# pass — placeholder for future code
print("Layers needing detailed analysis:")
for d, n in zip(depths, n_values):
    if n < 10:
        pass  # TODO: add detailed settlement calculation later
        print(f"  {d:.1f}m (N={n}) — needs settlement analysis [placeholder]")

print()

# ══════════════════════════════════════════════════════════════
# PART 7: NESTED LOOPS — Multi-Borehole Processing
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 7: NESTED LOOPS — Multiple Boreholes")
print("=" * 60)

# Data from 3 boreholes
boreholes = {
    "BH-01": [5, 8, 18, 35, 50],
    "BH-02": [3, 6, 14, 22, 45],
    "BH-03": [7, 12, 25, 40, 55],
}

borehole_depths = [1.5, 3.0, 4.5, 6.0, 7.5]

print("Multi-Borehole N-value Summary:")
print(f"  {'BH':>6s}", end="")
for d in borehole_depths:
    print(f"  {d:5.1f}m", end="")
print("  | Avg N")
print("  " + "─" * 52)

for bh_name, n_list in boreholes.items():
    avg_n = sum(n_list) / len(n_list)
    print(f"  {bh_name}", end="")
    for n in n_list:
        print(f"  {n:5d} ", end="")
    print(f"  | {avg_n:.1f}")

print()

# ══════════════════════════════════════════════════════════════
# PART 8: ACCUMULATOR PATTERNS — Statistics from Loops
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 8: ACCUMULATOR PATTERNS — Loop Statistics")
print("=" * 60)

n_values_all = [5, 8, 12, 18, 28, 35, 50, 60]

# Sum
total = 0
for n in n_values_all:
    total += n
average = total / len(n_values_all)
print(f"Sum of N-values: {total}")
print(f"Average N-value: {average:.1f}")

# Min and Max
n_min = n_values_all[0]
n_max = n_values_all[0]
for n in n_values_all:
    if n < n_min:
        n_min = n
    if n > n_max:
        n_max = n
print(f"Min N: {n_min}, Max N: {n_max}")

# Count layers above/below threshold
weak = 0
strong = 0
threshold = 15
for n in n_values_all:
    if n < threshold:
        weak += 1
    else:
        strong += 1
print(f"Weak layers (N<{threshold}): {weak}")
print(f"Strong layers (N>={threshold}): {strong}")

# Build a new list (will use list comprehension in Day 005)
vs_values = []
for n in n_values_all:
    vs = 97 * (n ** 0.314)
    vs_values.append(vs)

print(f"\nEstimated Vs (m/s) for each layer:")
for d, vs in zip(depths, vs_values):
    print(f"  {d:5.1f}m → Vs = {vs:.1f} m/s")

print()

# ══════════════════════════════════════════════════════════════
# PART 9: COMPLETE APPLICATION — Automated Borehole Report
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  AUTOMATED BOREHOLE REPORT — BH-01")
print("  Salt Lake City, Utah | Water Table: 3.2m")
print("=" * 60)

depths =     [1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0]
n_values =   [5,   8,   12,  18,  28,  35,  50,   60]
soil_types = ["Fill", "Silty Sand", "Sand", "Clayey Sand",
              "Sand", "Gravel", "Weathered Rock", "Bedrock"]
wt = 3.2

# Header
print(f"  {'#':>2s}  {'Depth':>6s}  {'N60':>4s}  {'Soil':16s}  {'Consistency':13s}  {'Sat':3s}  {'Vs(m/s)':>7s}  Liq")
print("  " + "─" * 75)

# Accumulators
total_n = 0
liq_warnings = 0
bearing_depth = None
vs_list = []

# Main processing loop
for i, (d, n, s) in enumerate(zip(depths, n_values, soil_types), start=1):
    
    # Consistency (if/elif/else)
    if n < 4:
        cons = "Very Loose"
    elif n < 10:
        cons = "Loose"
    elif n < 30:
        cons = "Medium Dense"
    elif n < 50:
        cons = "Dense"
    else:
        cons = "Very Dense"
    
    # Saturation (comparison)
    sat = "Y" if d > wt else "N"
    
    # Vs estimation
    vs = 97 * (n ** 0.314)
    vs_list.append(vs)
    
    # Liquefaction screening (logical operators)
    if d > wt and n < 20 and "Sand" in s and d < 20:
        liq = "CHECK"
        liq_warnings += 1
    else:
        liq = "OK"
    
    # Track first bearing layer
    if bearing_depth is None and n >= 15:
        bearing_depth = d
    
    # Accumulate
    total_n += n
    
    # Print row
    print(f"  {i:2d}  {d:5.1f}m  {n:4d}  {s:16s}  {cons:13s}  {sat:3s}  {vs:7.1f}  {liq}")

# Summary statistics
print("  " + "─" * 75)
avg_n = total_n / len(n_values)
avg_vs = sum(vs_list) / len(vs_list)
min_n = min(n_values)
max_n = max(n_values)

print(f"\n  STATISTICS:")
print(f"  Average N60  : {avg_n:.1f}")
print(f"  Range N60    : {min_n} — {max_n}")
print(f"  Average Vs   : {avg_vs:.1f} m/s")
print(f"  Vs30 (approx): {avg_vs:.1f} m/s")

print(f"\n  RECOMMENDATIONS:")
if liq_warnings > 0:
    print(f"  ⚠ {liq_warnings} layer(s) require liquefaction analysis")
if bearing_depth:
    print(f"  ✓ Suitable bearing layer at {bearing_depth:.1f}m depth")
else:
    print(f"  ⚠ No suitable bearing layer found — consider piles")

print("=" * 60)
print("  Day 003 Complete!")
print("=" * 60)
