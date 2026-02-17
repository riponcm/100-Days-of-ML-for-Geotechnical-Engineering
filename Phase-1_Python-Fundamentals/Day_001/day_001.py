"""
Day 001: Variables, Data Types & Type Casting
100 Days of ML for Geotechnical Engineering
Phase: Python Fundamentals

Author: Ripon Chandra Malo
Date: February 16, 2026

Geotechnical Problem: SPT Borehole Log Data Entry & Analysis
─────────────────────────────────────────────────────────────
We received field data from a Standard Penetration Test (SPT)
borehole investigation. Our job is to store, organize, and
perform basic calculations on this data using Python.
"""

# ══════════════════════════════════════════════════════════════
# PART 1: VARIABLES — Storing Borehole Information
# ══════════════════════════════════════════════════════════════

# --- Project Information ---
project_name = "Highway Bridge Foundation Investigation"
project_id = "GE-2026-0042"
location = "Salt Lake City, Utah"
borehole_id = "BH-01"

# --- Borehole Parameters ---
borehole_depth = 15.5          # meters (float)
water_table_depth = 3.2        # meters (float)
number_of_samples = 8          # count (integer)
ground_elevation = 1320.75     # meters above sea level (float)

# --- SPT Data at 3.0m depth ---
spt_n_value = 18               # blow count (integer)
sample_depth = 3.0             # meters (float)
soil_type = "Silty Sand"       # classification (string)
is_saturated = False           # below water table? (boolean)

print("=" * 55)
print("  BOREHOLE LOG SUMMARY")
print("=" * 55)
print(f"Project    : {project_name}")
print(f"Borehole   : {borehole_id}")
print(f"Location   : {location}")
print(f"Total Depth: {borehole_depth} m")
print(f"Water Table: {water_table_depth} m")
print(f"Samples    : {number_of_samples}")
print()

# ══════════════════════════════════════════════════════════════
# PART 2: DATA TYPES — Understanding What We Store
# ══════════════════════════════════════════════════════════════

print("─" * 55)
print("  DATA TYPES CHECK")
print("─" * 55)
print(f"project_name      = {project_name!r:>30} → {type(project_name).__name__}")
print(f"borehole_depth     = {borehole_depth!r:>30} → {type(borehole_depth).__name__}")
print(f"spt_n_value        = {spt_n_value!r:>30} → {type(spt_n_value).__name__}")
print(f"is_saturated       = {is_saturated!r:>30} → {type(is_saturated).__name__}")
print()

# --- Why data types matter in geotechnical engineering ---
# int   → SPT N-value (always whole numbers: 5, 12, 28, 50)
# float → depths, elevations, unit weights (3.2m, 18.5 kN/m³)
# str   → soil descriptions, classifications ("Silty Sand", "CL")
# bool  → yes/no conditions (saturated?, liquefiable?, stable?)


# ══════════════════════════════════════════════════════════════
# PART 3: TYPE CASTING — Converting Field Data
# ══════════════════════════════════════════════════════════════

print("─" * 55)
print("  TYPE CASTING — Real Scenarios")
print("─" * 55)

# Scenario 1: Field engineer sends SPT N-value as text (from form)
field_n_value = "24"                     # came as string from field form
n_value_int = int(field_n_value)         # convert to integer for calculation
print(f"Field data (string): '{field_n_value}' → integer: {n_value_int}")

# Scenario 2: Depth recorded as integer, need decimal precision
recorded_depth = 7                       # field crew wrote "7" not "7.0"
precise_depth = float(recorded_depth)    # convert for calculation
print(f"Recorded depth: {recorded_depth} → precise: {precise_depth} m")

# Scenario 3: Generate a report label from numbers
layer_number = 3
depth_value = 4.5
label = "Layer-" + str(layer_number) + " at " + str(depth_value) + "m"
print(f"Report label: {label}")

# Scenario 4: Check if a value exists (truthiness)
n_value_zero = 0        # weight-of-hammer (very soft soil)
n_value_normal = 15
print(f"N=0 as boolean: {bool(n_value_zero)} (means: no resistance!)")
print(f"N=15 as boolean: {bool(n_value_normal)} (means: soil has strength)")
print()

# ══════════════════════════════════════════════════════════════
# PART 4: GEOTECHNICAL APPLICATION
# Basic SPT Correlation — Estimating Soil Properties
# ══════════════════════════════════════════════════════════════

print("=" * 55)
print("  SPT CORRELATION CALCULATIONS")
print("=" * 55)

# Given SPT data from field
N_field = "22"             # came as string from digital form
depth_str = "6.5"          # came as string from GPS logger
hammer_efficiency = "60"   # percentage, as string

# Step 1: Type casting — convert strings to numbers
N = int(N_field)
depth = float(depth_str)
Ce = int(hammer_efficiency) / 100   # efficiency ratio (float division)

print(f"Raw field N-value : {N_field} (string) → {N} (int)")
print(f"Depth             : {depth_str} (string) → {depth} (float) m")
print(f"Hammer efficiency : {hammer_efficiency}% → {Ce} (ratio)")

# Step 2: SPT N-value correction (N60)
# N60 = N × (Ce / 0.60)
N60 = N * (Ce / 0.60)
print(f"\nCorrected N60 = {N} × ({Ce}/0.60) = {N60:.1f}")

# Step 3: Overburden pressure correction (simplified)
# Assume unit weight = 18.5 kN/m³
unit_weight = 18.5                           # kN/m³
overburden_pressure = unit_weight * depth     # kN/m²
print(f"Overburden pressure = {unit_weight} × {depth} = {overburden_pressure:.1f} kN/m²")

# Step 4: Estimate Shear Wave Velocity (Vs) from SPT
# Imai & Tonouchi (1982): Vs = 97 × N^0.314
Vs = 97 * (N60 ** 0.314)
print(f"Estimated Vs = 97 × {N60:.1f}^0.314 = {Vs:.1f} m/s")

# Step 5: Soil classification based on N-value
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

print(f"Soil consistency: {consistency}")

# Step 6: Saturation check
is_below_wt = depth > water_table_depth
print(f"\nDepth ({depth}m) > Water table ({water_table_depth}m)? → {is_below_wt}")
if is_below_wt:
    print("⚠ Sample is SATURATED — consider liquefaction potential!")
else:
    print("Sample is above water table — not saturated")

print()
print("=" * 55)
print("  Day 001 Complete!")
print("=" * 55)
