"""
Day 002: Conditionals — if / elif / else
100 Days of ML for Geotechnical Engineering
Phase: Python Fundamentals

Author: Ripon Chandra Malo
Date: February 17, 2026

Geotechnical Problem: Automated Soil Classification & Safety Checks
────────────────────────────────────────────────────────────────────
We have SPT borehole data from multiple depths. Our job is to write
decision-making logic that automatically classifies soil consistency,
checks safety conditions, and flags problematic layers — exactly
what a geotechnical engineer does mentally when reading a borehole log.
"""

# ══════════════════════════════════════════════════════════════
# PART 1: BASIC if / else — Is This Layer Saturated?
# ══════════════════════════════════════════════════════════════

# Borehole parameters
water_table_depth = 3.2  # meters
sample_depth = 6.5       # meters

print("=" * 55)
print("  PART 1: BASIC if / else")
print("=" * 55)

if sample_depth > water_table_depth:
    is_saturated = True
    print(f"Depth {sample_depth}m > Water table {water_table_depth}m")
    print("→ Layer is SATURATED")
else:
    is_saturated = False
    print(f"Depth {sample_depth}m <= Water table {water_table_depth}m")
    print("→ Layer is DRY")

print()

# ══════════════════════════════════════════════════════════════
# PART 2: if / elif / else — Soil Consistency from SPT N-value
# ══════════════════════════════════════════════════════════════

# IS 1893 / Terzaghi classification for granular soils
N60 = 22.0

print("=" * 55)
print("  PART 2: if / elif / else — Soil Consistency")
print("=" * 55)

if N60 < 4:
    consistency = "Very Loose"
    risk_level = "HIGH"
elif N60 < 10:
    consistency = "Loose"
    risk_level = "MODERATE"
elif N60 < 30:
    consistency = "Medium Dense"
    risk_level = "LOW"
elif N60 < 50:
    consistency = "Dense"
    risk_level = "VERY LOW"
else:
    consistency = "Very Dense"
    risk_level = "NEGLIGIBLE"

print(f"N60 = {N60}")
print(f"Consistency: {consistency}")
print(f"Settlement Risk: {risk_level}")
print()

# ══════════════════════════════════════════════════════════════
# PART 3: NESTED if — Liquefaction Screening
# ══════════════════════════════════════════════════════════════

print("=" * 55)
print("  PART 3: NESTED if — Liquefaction Screening")
print("=" * 55)

soil_type = "Sand"
depth = 6.5
N60 = 15.0
is_saturated = True
earthquake_zone = True

# Liquefaction needs ALL these conditions:
# 1. Sandy or silty soil
# 2. Below water table (saturated)
# 3. Shallow depth (< 20m typically)
# 4. Low N-value
# 5. In a seismic zone

if earthquake_zone:
    print("Step 1: Site is in earthquake zone ✓")
    if soil_type in ("Sand", "Silty Sand", "Sandy Silt"):
        print(f"Step 2: Soil type is {soil_type} (liquefiable type) ✓")
        if is_saturated:
            print("Step 3: Layer is saturated ✓")
            if depth < 20.0:
                print(f"Step 4: Depth {depth}m < 20m (critical zone) ✓")
                if N60 < 20:
                    print(f"Step 5: N60={N60} < 20 (low resistance) ✓")
                    print()
                    print("⚠ LIQUEFACTION RISK: HIGH")
                    print("→ Detailed analysis required (Seed & Idriss method)")
                else:
                    print(f"Step 5: N60={N60} >= 20 → Adequate resistance")
                    print("→ Liquefaction risk: LOW")
            else:
                print(f"Step 4: Depth {depth}m >= 20m → Too deep for liquefaction")
        else:
            print("Step 3: Layer is NOT saturated → No liquefaction risk")
    else:
        print(f"Step 2: {soil_type} is not a liquefiable soil type")
else:
    print("Step 1: Not in earthquake zone → No liquefaction analysis needed")

print()

# ══════════════════════════════════════════════════════════════
# PART 4: COMPARISON OPERATORS — Engineering Checks
# ══════════════════════════════════════════════════════════════

print("=" * 55)
print("  PART 4: COMPARISON OPERATORS")
print("=" * 55)

bearing_capacity = 150.0   # kN/m² (allowable)
applied_load = 180.0       # kN/m² (from structure)

print(f"Bearing capacity: {bearing_capacity} kN/m²")
print(f"Applied load    : {applied_load} kN/m²")
print()
print(f"  load == capacity  : {applied_load == bearing_capacity}")
print(f"  load != capacity  : {applied_load != bearing_capacity}")
print(f"  load > capacity   : {applied_load > bearing_capacity}")
print(f"  load < capacity   : {applied_load < bearing_capacity}")
print(f"  load >= capacity  : {applied_load >= bearing_capacity}")
print(f"  load <= capacity  : {applied_load <= bearing_capacity}")
print()

if applied_load > bearing_capacity:
    FoS = bearing_capacity / applied_load
    print(f"⚠ OVERSTRESSED! Factor of Safety = {FoS:.2f} (< 1.0)")
    print("→ Foundation redesign required")
else:
    FoS = bearing_capacity / applied_load
    print(f"✓ SAFE. Factor of Safety = {FoS:.2f}")

print()

# ══════════════════════════════════════════════════════════════
# PART 5: LOGICAL OPERATORS — Combined Safety Checks
# ══════════════════════════════════════════════════════════════

print("=" * 55)
print("  PART 5: LOGICAL OPERATORS (and, or, not)")
print("=" * 55)

N60 = 8.0
depth = 5.0
is_saturated = True
has_fines = True        # fines content > 35%
seismic_zone = True

# AND — all conditions must be true
needs_liquefaction_check = is_saturated and (N60 < 20) and seismic_zone
print(f"Needs liquefaction check (all must be true):")
print(f"  saturated={is_saturated} AND N60<20={N60<20} AND seismic={seismic_zone}")
print(f"  → {needs_liquefaction_check}")
print()

# OR — at least one condition must be true
needs_special_attention = (N60 < 4) or is_saturated or (depth < 2.0)
print(f"Needs special attention (any one true):")
print(f"  N60<4={N60<4} OR saturated={is_saturated} OR shallow={depth<2.0}")
print(f"  → {needs_special_attention}")
print()

# NOT — invert a condition
is_dry = not is_saturated
print(f"is_saturated = {is_saturated}")
print(f"is_dry = not is_saturated = {is_dry}")
print()

# Combined real check
if is_saturated and (N60 < 15) and seismic_zone and (not has_fines):
    print("→ Clean sand, saturated, low N, seismic zone")
    print("→ HIGHEST liquefaction risk!")
elif is_saturated and (N60 < 15) and seismic_zone and has_fines:
    print("→ Sandy soil with fines, saturated, low N, seismic zone")
    print("→ MODERATE liquefaction risk (fines may help)")
else:
    print("→ Liquefaction risk appears manageable")

print()

# ══════════════════════════════════════════════════════════════
# PART 6: TERNARY OPERATOR — Quick One-Line Decisions
# ══════════════════════════════════════════════════════════════

print("=" * 55)
print("  PART 6: TERNARY (ONE-LINE if/else)")
print("=" * 55)

N60 = 35.0
status = "Suitable" if N60 >= 15 else "Not Suitable"
print(f"N60 = {N60} → Foundation status: {status}")

depth = 2.5
wt = 3.2
condition = "Saturated" if depth > wt else "Dry"
print(f"Depth={depth}m, WT={wt}m → {condition}")

FoS = 2.3
safety = "SAFE" if FoS >= 1.5 else ("MARGINAL" if FoS >= 1.0 else "UNSAFE")
print(f"FoS = {FoS} → {safety}")
print()

# ══════════════════════════════════════════════════════════════
# PART 7: COMPLETE APPLICATION — Multi-Layer Borehole Assessment
# ══════════════════════════════════════════════════════════════

print("=" * 55)
print("  COMPLETE BOREHOLE SAFETY ASSESSMENT")
print("=" * 55)
print(f"  Borehole: BH-01 | Location: Salt Lake City, Utah")
print(f"  Water Table: 3.2 m | Seismic Zone: Yes")
print("─" * 55)

# Layer data (simulating what we'll do with lists in Day 005)
layers = [
    {"depth": 1.5, "N60": 5,  "soil": "Fill",       "fines": 40},
    {"depth": 3.0, "N60": 8,  "soil": "Silty Sand",  "fines": 25},
    {"depth": 6.0, "N60": 18, "soil": "Sand",         "fines": 8},
    {"depth": 9.0, "N60": 35, "soil": "Dense Sand",   "fines": 5},
    {"depth": 12.0,"N60": 50, "soil": "Gravel",       "fines": 3},
    {"depth": 15.0,"N60": 60, "soil": "Weathered Rock","fines": 0},
]

wt = 3.2
seismic = True
warnings = 0

for layer in layers:
    d = layer["depth"]
    n = layer["N60"]
    s = layer["soil"]
    fc = layer["fines"]

    # Consistency
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

    # Saturation
    sat = "Yes" if d > wt else "No"

    # Liquefaction flag
    if (d > wt) and (n < 20) and seismic and (fc < 35) and (d < 20):
        liq = "⚠ CHECK"
        warnings += 1
    else:
        liq = "OK"

    # Foundation suitability
    suitable = "Yes" if n >= 15 else "No"

    print(f"  {d:5.1f}m | N60={n:3d} | {s:16s} | {cons:13s} | Sat:{sat:3s} | Liq:{liq:7s} | Found:{suitable}")

print("─" * 55)

if warnings > 0:
    print(f"  ⚠ {warnings} layer(s) flagged for liquefaction analysis!")
    print("  → Recommend Seed & Idriss simplified procedure")
else:
    print("  ✓ No liquefaction concerns identified")

if any(layer["N60"] >= 15 for layer in layers if layer["depth"] > 3.0):
    print("  ✓ Suitable bearing layer found below 3.0m")
else:
    print("  ⚠ No suitable bearing layer — consider deep foundation")

print("=" * 55)
print("  Day 002 Complete!")
print("=" * 55)
