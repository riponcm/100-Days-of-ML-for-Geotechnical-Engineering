"""
Day 007: Functions & Lambda Expressions
100 Days of ML for Geotechnical Engineering
Phase: Python Fundamentals

Author: Ripon Chandra Malo
Date: February 22, 2026

Geotechnical Problem: Building a Reusable SPT Analysis Toolkit
──────────────────────────────────────────────────────────────
On Days 001-006, we kept writing the SAME code over and over:
  - Classify soil:       if N60 < 4: ... elif N60 < 10: ...
  - Estimate Vs:         97 * (N60 ** 0.314)
  - Check saturation:    depth > water_table
  - Compute overburden:  gamma * depth

Every time we needed these, we copied the whole block. What if
we had 100 boreholes? 1000 layers? Copy-pasting would be a nightmare.

FUNCTIONS solve this: write the logic ONCE, call it FOREVER.

Think of a function like a LAB TEST MACHINE:
  1. You FEED it a sample      → parameters (input)
  2. The machine PROCESSES it  → function body (logic)
  3. It RETURNS a report       → return value (output)

You build the machine once. Then you feed it any sample, any time.
"""

# ══════════════════════════════════════════════════════════════
# PART 1: YOUR FIRST FUNCTION — The Basics
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 1: YOUR FIRST FUNCTION")
print("=" * 60)

# A function is defined with 'def', a name, and parentheses.
# The code inside (indented) runs when you CALL the function.

# STEP 1: DEFINE the function (build the machine)
def print_report_header():
    """Prints a standard report header."""
    print("╔══════════════════════════════════════════╗")
    print("║    GEOTECHNICAL INVESTIGATION REPORT     ║")
    print("║    Standard Penetration Test (SPT)       ║")
    print("╚══════════════════════════════════════════╝")

# STEP 2: CALL the function (use the machine)
print_report_header()
print()

# Call it again — same result, zero code duplication
print("Calling the same function again:")
print_report_header()
print()

# Key anatomy:
# def  function_name():    ← 'def' keyword + name + colon
#     """docstring"""       ← optional description
#     code                  ← indented body (what it does)
#     code
#
# function_name()           ← call it by name + parentheses


# ══════════════════════════════════════════════════════════════
# PART 2: PARAMETERS — Giving Functions Input
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 2: PARAMETERS (Input)")
print("=" * 60)

# Most functions need INPUT to work with.
# Parameters are PLACEHOLDERS — they receive values when called.

# Think of it this way:
#   PARAMETER = the sample slot on the lab machine (accepts any sample)
#   ARGUMENT  = the actual soil sample you put in

def classify_granular(N60):
    """
    Classify granular soil consistency from SPT N60 value.
    
    This is the same if/elif chain from Day 002, but now
    wrapped in a function. Write once, use forever!
    """
    if N60 < 4:
        return "Very Loose"
    elif N60 < 10:
        return "Loose"
    elif N60 < 30:
        return "Medium Dense"
    elif N60 < 50:
        return "Dense"
    else:
        return "Very Dense"

# Now classify ANY N-value with ONE line!
print(f"N60=3  → {classify_granular(3)}")
print(f"N60=8  → {classify_granular(8)}")
print(f"N60=22 → {classify_granular(22)}")
print(f"N60=45 → {classify_granular(45)}")
print(f"N60=60 → {classify_granular(60)}")
print()

# Power of functions: use in a loop!
n_values = [3, 8, 18, 35, 55]
print("Classify a whole borehole:")
for n in n_values:
    print(f"  N60={n:3d} → {classify_granular(n)}")
print()

# Without functions: 5 layers × 10 lines each = 50 lines of if/elif
# With functions:    5 layers × 1 line each   = 5 lines
# 1000 layers?       Still just 1000 one-line calls inside a loop!


# ══════════════════════════════════════════════════════════════
# PART 3: RETURN VALUES — Getting Results Back
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 3: RETURN VALUES (Output)")
print("=" * 60)

# 'return' sends a value BACK to wherever the function was called.
# Without return, the function does work but gives you nothing back.

# Think of it like the lab:
#   You SEND a sample       → parameter
#   The lab PROCESSES it     → function body
#   The lab RETURNS a report → return value

def estimate_vs(N60):
    """Estimate shear wave velocity from N60 (Imai & Tonouchi, 1982)."""
    Vs = 97 * (N60 ** 0.314)
    return Vs

def overburden_pressure(depth, unit_weight):
    """Calculate vertical overburden pressure: σv = γ × z."""
    sigma_v = unit_weight * depth
    return sigma_v

# Call and STORE the returned value
Vs = estimate_vs(22)
sigma_v = overburden_pressure(6.5, 18.5)

print(f"Vs at N60=22: {Vs:.1f} m/s")
print(f"σv at 6.5m:   {sigma_v:.1f} kN/m²")
print()

# Chain function calls — use output of one as input to another
N60 = 22
Vs = estimate_vs(N60)
print(f"N60={N60} → Vs={Vs:.1f} m/s")

# Or even in one line:
print(f"Vs(30) = {estimate_vs(30):.1f} m/s")
print()

# What happens WITHOUT return?
def bad_function(N60):
    Vs = 97 * (N60 ** 0.314)
    # No return statement!

result = bad_function(22)
print(f"Without return: result = {result}")  # None!
print("Always use 'return' when you want to GET a value back!")
print()


# ══════════════════════════════════════════════════════════════
# PART 4: MULTIPLE PARAMETERS — Functions With Many Inputs
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 4: MULTIPLE PARAMETERS")
print("=" * 60)

def correct_n60(N_field, hammer_efficiency, borehole_diameter,
                rod_length, sampler_type):
    """
    Full SPT N-value correction: N60 = N_field × CE × CB × CR × CS
    
    Parameters:
        N_field           : Raw blow count from field
        hammer_efficiency : Hammer energy ratio (%) 
        borehole_diameter : Borehole diameter in mm
        rod_length        : Rod length in meters
        sampler_type      : "standard" or "liner"
    """
    # Hammer correction
    CE = hammer_efficiency / 60.0
    
    # Borehole diameter correction
    if borehole_diameter <= 115:
        CB = 1.0
    elif borehole_diameter <= 150:
        CB = 1.05
    else:
        CB = 1.15
    
    # Rod length correction
    if rod_length < 3:
        CR = 0.75
    elif rod_length < 4:
        CR = 0.80
    elif rod_length < 6:
        CR = 0.85
    elif rod_length < 10:
        CR = 0.95
    else:
        CR = 1.0
    
    # Sampler correction
    CS = 1.0 if sampler_type == "standard" else 1.2
    
    N60 = N_field * CE * CB * CR * CS
    return N60

# Use it
N60 = correct_n60(22, 60, 100, 8.0, "standard")
print(f"Corrected N60 = {N60:.1f}")

N60_auto = correct_n60(22, 80, 150, 12.0, "standard")
print(f"Auto hammer N60 = {N60_auto:.1f}")
print()


# ══════════════════════════════════════════════════════════════
# PART 5: DEFAULT PARAMETERS — Sensible Assumptions
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 5: DEFAULT PARAMETERS")
print("=" * 60)

# Default parameters have pre-set values. If you don't provide
# a value, the default is used. If you do, your value overrides it.

# Think of a FORM with pre-filled fields:
#   - Most projects use 60% efficiency → pre-fill with 60
#   - But you CAN change it to 80 for an auto hammer

def simple_n60(N_field, efficiency=60, diameter=100):
    """
    Simplified N60 correction with sensible defaults.
    
    Most SPT tests use:
      - 60% hammer efficiency (safety hammer)
      - 100mm borehole diameter
    
    Override only when your equipment differs.
    """
    CE = efficiency / 60.0
    CB = 1.0 if diameter <= 115 else 1.05 if diameter <= 150 else 1.15
    return N_field * CE * CB

# Use ALL defaults (most common case)
print(f"Defaults:          N60 = {simple_n60(22):.1f}")

# Override efficiency only (auto hammer)
print(f"Auto hammer (80%): N60 = {simple_n60(22, efficiency=80):.1f}")

# Override diameter only
print(f"Large bore (200mm): N60 = {simple_n60(22, diameter=200):.1f}")

# Override both
print(f"Custom:             N60 = {simple_n60(22, efficiency=75, diameter=150):.1f}")
print()

# RULE: Required parameters first, then optional with defaults
# def func(required1, required2, optional1=default, optional2=default)
# GOOD:  def func(N_field, efficiency=60)
# BAD:   def func(efficiency=60, N_field)  ← SyntaxError!


# ══════════════════════════════════════════════════════════════
# PART 6: MULTIPLE RETURN VALUES — One Function, Many Results
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 6: MULTIPLE RETURN VALUES")
print("=" * 60)

# Python functions can return SEVERAL values at once.
# Incredibly useful when one analysis produces multiple results.

def analyze_layer(N_field, depth, water_table, efficiency=60):
    """
    Complete SPT analysis for one layer.
    
    Takes raw field data, returns everything you need:
      N60, Vs, consistency, is_saturated, liquefaction_risk
    """
    # Correct N-value
    N60 = N_field * (efficiency / 60)
    
    # Estimate shear wave velocity
    Vs = 97 * (N60 ** 0.314)
    
    # Classify consistency
    if N60 < 4:     consistency = "Very Loose"
    elif N60 < 10:  consistency = "Loose"
    elif N60 < 30:  consistency = "Medium Dense"
    elif N60 < 50:  consistency = "Dense"
    else:           consistency = "Very Dense"
    
    # Check saturation
    is_saturated = depth > water_table
    
    # Simple liquefaction screening
    if is_saturated and N60 < 15:
        liq_risk = "HIGH"
    elif is_saturated and N60 < 25:
        liq_risk = "MODERATE"
    else:
        liq_risk = "LOW"
    
    return N60, Vs, consistency, is_saturated, liq_risk

# Call and UNPACK all 5 results
N60, Vs, cons, sat, liq = analyze_layer(22, 6.5, 3.2)
print(f"N60: {N60:.1f}")
print(f"Vs:  {Vs:.1f} m/s")
print(f"Class: {cons}")
print(f"Saturated: {sat}")
print(f"Liquefaction: {liq}")
print()

# Use in a loop — process ALL layers at once
depths  = [1.5, 3.0, 4.5, 6.0, 7.5, 9.0]
n_raw   = [5,   8,   12,  18,  28,  35]
wt = 3.2

print(f"  {'#':>2} {'Dep':>5} {'N60':>5} {'Vs':>6} {'Class':13s} {'Sat':>3} {'Liq':>4}")
print("  " + "─" * 52)
for i, (d, n) in enumerate(zip(depths, n_raw), start=1):
    N60, Vs, cons, sat, liq = analyze_layer(n, d, wt)
    s_flag = "Y" if sat else "N"
    print(f"  {i:2d} {d:4.1f}m {N60:5.1f} {Vs:5.1f} {cons:13s} {s_flag:>3} {liq:>4}")
print()


# ══════════════════════════════════════════════════════════════
# PART 7: RETURNING DICTIONARIES — Named Results
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 7: RETURNING DICTIONARIES")
print("=" * 60)

# When a function returns many values, a dictionary keeps them organized.
# Instead of remembering the ORDER of 5+ return values, access by NAME.

def full_layer_analysis(N_field, depth, soil_type, water_table, efficiency=60):
    """Complete layer analysis returning a labeled dictionary."""
    N60 = N_field * (efficiency / 60)
    Vs = 97 * (N60 ** 0.314)
    sigma_v = 18.5 * depth
    Dr = 21 * (N60 ** 0.5)
    
    if N60 < 4:     cons = "Very Loose"
    elif N60 < 10:  cons = "Loose"
    elif N60 < 30:  cons = "Medium Dense"
    elif N60 < 50:  cons = "Dense"
    else:           cons = "Very Dense"
    
    return {
        "depth": depth,
        "N60": N60,
        "Vs": round(Vs, 1),
        "sigma_v": round(sigma_v, 1),
        "Dr": round(Dr, 1),
        "consistency": cons,
        "soil": soil_type,
        "saturated": depth > water_table,
    }

# Get a complete analysis as a dictionary
result = full_layer_analysis(22, 6.0, "Sand", 3.2)
print("Result dictionary:")
for key, value in result.items():
    print(f"  {key:13s} = {value}")
print()

# Access specific results by name — much clearer than index!
print(f"Vs = {result['Vs']} m/s")
print(f"Is it saturated? {result['saturated']}")
print()


# ══════════════════════════════════════════════════════════════
# PART 8: DOCSTRINGS — Your Future Self Will Thank You
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 8: DOCSTRINGS")
print("=" * 60)

def liquefaction_screening(N60, depth, water_table, magnitude=7.5):
    """
    Screen a soil layer for liquefaction susceptibility.
    
    Uses simplified procedure based on Seed & Idriss (1971).
    
    Parameters
    ----------
    N60 : float
        Corrected SPT blow count
    depth : float
        Sample depth in meters
    water_table : float
        Water table depth in meters
    magnitude : float, optional
        Design earthquake magnitude (default: 7.5)
    
    Returns
    -------
    dict
        Dictionary with keys:
        - 'risk': str — "HIGH", "MODERATE", "LOW", or "NONE"
        - 'CSR': float — Cyclic Stress Ratio
        - 'CRR': float — Cyclic Resistance Ratio
        - 'FoS': float — Factor of Safety against liquefaction
    """
    is_saturated = depth > water_table
    
    if not is_saturated or N60 > 30:
        return {"risk": "NONE", "CSR": 0, "CRR": 0, "FoS": float('inf')}
    
    # Simplified CSR (Seed & Idriss)
    sigma_v = 18.5 * depth
    sigma_v_eff = sigma_v - 9.81 * max(0, depth - water_table)
    amax = 0.3  # assumed PGA
    rd = max(0, 1.0 - 0.00765 * depth) if depth <= 9.15 else max(0, 1.174 - 0.0267 * depth)
    CSR = 0.65 * (sigma_v / sigma_v_eff) * amax * rd
    
    # Simplified CRR
    CRR = 1 / (34 - N60) + N60 / 135 + 50 / (10 * N60 + 45) ** 2 - 1 / 200
    
    # Factor of Safety
    FoS = CRR / CSR if CSR > 0 else float('inf')
    
    if FoS < 1.0:
        risk = "HIGH"
    elif FoS < 1.25:
        risk = "MODERATE"
    elif FoS < 1.5:
        risk = "LOW"
    else:
        risk = "NONE"
    
    return {"risk": risk, "CSR": round(CSR, 3), "CRR": round(CRR, 3), "FoS": round(FoS, 2)}

# Access the documentation
print("Function documentation:")
print(liquefaction_screening.__doc__[:300] + "...")
print()

# Use it
result = liquefaction_screening(12, 5.0, 2.0)
print(f"Liquefaction check at 5m, N60=12:")
print(f"  Risk: {result['risk']}")
print(f"  CSR:  {result['CSR']}")
print(f"  CRR:  {result['CRR']}")
print(f"  FoS:  {result['FoS']}")
print()


# ══════════════════════════════════════════════════════════════
# PART 9: VARIABLE SCOPE — Local vs Global
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 9: VARIABLE SCOPE")
print("=" * 60)

# Variables created INSIDE a function are LOCAL — they only
# exist during that function call. Once the function ends, they die.
#
# Variables created OUTSIDE functions are GLOBAL — accessible everywhere.

project_name = "Highway Bridge"  # GLOBAL — exists everywhere

def calculate_settlement(N60, load):
    """Variables inside are LOCAL."""
    factor = 0.1          # LOCAL — only exists inside this function
    settlement = factor * load / N60
    return settlement

s = calculate_settlement(22, 150)
print(f"Settlement: {s:.2f} mm")
print(f"Project: {project_name}")   # GLOBAL → works

# Uncomment to see the error:
# print(factor)  # NameError! 'factor' is LOCAL — it doesn't exist here.

print()
print("LOCAL  = born inside function, dies when function ends")
print("GLOBAL = born outside function, accessible everywhere")
print("This is GOOD: functions don't pollute your main code.")
print()


# ══════════════════════════════════════════════════════════════
# PART 10: LAMBDA — Quick One-Line Functions
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 10: LAMBDA FUNCTIONS")
print("=" * 60)

# Lambda is a shortcut for creating SIMPLE functions in ONE LINE.
# Use when the function is so simple it doesn't deserve a name.

# Regular function (3 lines):
def vs_regular(N60):
    return 97 * (N60 ** 0.314)

# Lambda function (1 line):
vs_lambda = lambda N60: 97 * (N60 ** 0.314)

# Both do exactly the same thing
print(f"Regular: Vs(22) = {vs_regular(22):.1f} m/s")
print(f"Lambda:  Vs(22) = {vs_lambda(22):.1f} m/s")
print()

# More lambda examples
overburden = lambda depth, gamma=18.5: gamma * depth
classify_quick = lambda n: "Dense+" if n >= 30 else "Med" if n >= 10 else "Loose"
is_saturated = lambda depth, wt: depth > wt

print(f"Overburden at 6m: {overburden(6.0):.1f} kN/m²")
print(f"Classify N=25: {classify_quick(25)}")
print(f"Saturated at 5m (wt=3.2)? {is_saturated(5.0, 3.2)}")
print()

# Lambda shines with map(), sorted(), and list comprehension
n_values = [5, 12, 22, 35, 50]

# Apply to every item
vs_list = list(map(lambda n: round(97 * (n ** 0.314), 1), n_values))
print(f"N-values: {n_values}")
print(f"Vs (map): {vs_list}")
print()

# Sort layers by N-value (lambda as sort key)
layers = [("Sand", 6.0, 18), ("Fill", 1.5, 5), ("Clay", 3.0, 8), ("Rock", 12.0, 60)]

by_depth = sorted(layers, key=lambda x: x[1])
by_strength = sorted(layers, key=lambda x: x[2], reverse=True)

print(f"By depth:    {by_depth}")
print(f"By strength: {by_strength}")
print()

# Sort list of dicts by N60
layer_dicts = [
    {"soil": "Fill", "N60": 5},
    {"soil": "Sand", "N60": 22},
    {"soil": "Clay", "N60": 8},
    {"soil": "Gravel", "N60": 35},
]
sorted_layers = sorted(layer_dicts, key=lambda d: d["N60"])
print("Sorted by N60:")
for l in sorted_layers:
    print(f"  {l['soil']:8s} N60={l['N60']}")
print()

# RULE OF THUMB:
# Simple calculation → lambda
# Complex logic (if/elif, multiple lines) → regular def
print("Lambda = simple one-liners. Use 'def' for complex logic.")
print()


# ══════════════════════════════════════════════════════════════
# PART 11: FUNCTIONS CALLING FUNCTIONS — Building Pipelines
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 11: FUNCTIONS CALLING FUNCTIONS")
print("=" * 60)

# Real engineering software is built by combining small functions.
# Each function does ONE thing well. Then you chain them together.

def correct_n(N_field, efficiency=60):
    """Step 1: Correct raw N for efficiency."""
    return N_field * (efficiency / 60)

def calc_vs(N60):
    """Step 2: Estimate Vs."""
    return 97 * (N60 ** 0.314)

def calc_overburden(depth, gamma=18.5):
    """Step 3: Overburden pressure."""
    return gamma * depth

def classify(N60):
    """Step 4: Classify consistency."""
    if N60 < 4: return "Very Loose"
    elif N60 < 10: return "Loose"
    elif N60 < 30: return "Medium Dense"
    elif N60 < 50: return "Dense"
    return "Very Dense"

def site_class_from_vs30(Vs30):
    """Step 5: ASCE 7 Site Class."""
    if Vs30 > 1500: return "A"
    elif Vs30 > 760: return "B"
    elif Vs30 > 360: return "C"
    elif Vs30 > 180: return "D"
    return "E"

# Pipeline: Chain functions together
N60 = correct_n(22, efficiency=60)
Vs = calc_vs(N60)
sigma_v = calc_overburden(6.0)
cons = classify(N60)

print(f"Pipeline: N_raw=22 → N60={N60:.1f} → Vs={Vs:.1f} → {cons} → σv={sigma_v:.1f}")
print()


# ══════════════════════════════════════════════════════════════
# MINI PROJECT 1: SPT BOREHOLE PROCESSOR
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  MINI PROJECT 1: SPT BOREHOLE PROCESSOR")
print("=" * 60)

def process_borehole(depths, n_raw, soils, water_table, bh_id="BH-01"):
    """
    Process an entire borehole using our toolkit functions.
    
    Input:  raw field data (lists)
    Output: list of processed layer dictionaries + summary
    """
    processed = []
    
    for d, n, s in zip(depths, n_raw, soils):
        N60 = correct_n(n)
        Vs = calc_vs(N60)
        sigma_v = calc_overburden(d)
        cons = classify(N60)
        sat = d > water_table
        
        processed.append({
            "depth": d, "N60": N60, "Vs": round(Vs, 1),
            "sigma_v": round(sigma_v, 1), "consistency": cons,
            "soil": s, "saturated": sat
        })
    
    # Summary
    all_vs = [l["Vs"] for l in processed]
    all_n = [l["N60"] for l in processed]
    avg_vs = sum(all_vs) / len(all_vs)
    
    summary = {
        "bh_id": bh_id,
        "layers": len(processed),
        "avg_n": round(sum(all_n) / len(all_n), 1),
        "avg_vs": round(avg_vs, 1),
        "site_class": site_class_from_vs30(avg_vs),
        "weak_layers": len([n for n in all_n if n < 15]),
    }
    
    return processed, summary

# Process BH-01
depths =   [1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0]
n_raw =    [5, 8, 12, 18, 28, 35, 50, 60]
soils =    ["Fill", "Silty Sand", "Sand", "Clayey Sand",
            "Sand", "Gravel", "Weathered Rock", "Bedrock"]

layers, summary = process_borehole(depths, n_raw, soils, 3.2, "BH-01")

print(f"  {summary['bh_id']} Summary:")
print(f"    Layers: {summary['layers']} | Avg N: {summary['avg_n']}")
print(f"    Avg Vs: {summary['avg_vs']} m/s | Site Class: {summary['site_class']}")
print(f"    Weak layers: {summary['weak_layers']}")
print()

# Print the table
print(f"  {'#':>2} {'Dep':>5} {'N60':>5} {'Soil':16s} {'Class':13s} {'Vs':>6} Sat")
print("  " + "─" * 56)
for i, l in enumerate(layers, 1):
    s_flag = "Y" if l["saturated"] else "N"
    print(f"  {i:2d} {l['depth']:4.1f}m {l['N60']:5.1f} {l['soil']:16s} "
          f"{l['consistency']:13s} {l['Vs']:5.1f} {s_flag:>3}")
print()


# ══════════════════════════════════════════════════════════════
# MINI PROJECT 2: BEARING CAPACITY CALCULATOR
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  MINI PROJECT 2: BEARING CAPACITY CALCULATOR")
print("=" * 60)

def bearing_capacity_meyerhof(N60, Df, B, foundation_shape="strip"):
    """
    Allowable bearing capacity using Meyerhof (1965) method.
    
    Parameters:
        N60              : Corrected SPT value
        Df               : Foundation depth (m)
        B                : Foundation width (m)
        foundation_shape : "strip" or "square"
    
    Returns:
        dict with q_net (kPa), q_allow (kPa), FoS used
    """
    if foundation_shape == "strip":
        if Df / B <= 1:
            q_net = 12 * N60 * (1 + 0.33 * Df / B)
        else:
            q_net = 12 * N60 * 1.33
    else:  # square
        if Df / B <= 1:
            q_net = 8 * N60 * (1 + 0.33 * Df / B)
        else:
            q_net = 8 * N60 * 1.33
    
    q_allow = q_net / 3.0  # FoS = 3
    
    return {
        "q_net": round(q_net, 1),
        "q_allow": round(q_allow, 1),
        "FoS": 3.0,
        "shape": foundation_shape,
        "N60": N60,
        "Df": Df,
        "B": B
    }

def check_safety(applied_load, capacity):
    """Check if foundation is safe."""
    FoS = capacity / applied_load if applied_load > 0 else float('inf')
    if FoS < 1.0:   status = "FAILURE"
    elif FoS < 1.5:  status = "MARGINAL"
    elif FoS < 3.0:  status = "SAFE"
    else:            status = "OVER-DESIGNED"
    return round(FoS, 2), status

# Design scenarios
scenarios = [
    {"N60": 15, "Df": 1.5, "B": 2.0, "shape": "strip",  "load": 120},
    {"N60": 15, "Df": 1.5, "B": 2.0, "shape": "square", "load": 120},
    {"N60": 25, "Df": 2.0, "B": 3.0, "shape": "strip",  "load": 180},
    {"N60": 35, "Df": 2.0, "B": 2.5, "shape": "square", "load": 200},
]

print(f"  {'N60':>4} {'Df':>4} {'B':>4} {'Shape':>6} {'q_allow':>8} {'Load':>5} {'FoS':>5} Status")
print("  " + "─" * 50)

for s in scenarios:
    result = bearing_capacity_meyerhof(s["N60"], s["Df"], s["B"], s["shape"])
    FoS, status = check_safety(s["load"], result["q_allow"])
    print(f"  {s['N60']:4d} {s['Df']:3.1f}m {s['B']:3.1f}m {s['shape']:>6s} "
          f"{result['q_allow']:7.1f} {s['load']:5d} {FoS:5.2f} {status}")
print()


# ══════════════════════════════════════════════════════════════
# MINI PROJECT 3: MULTI-BOREHOLE SITE COMPARATOR
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  MINI PROJECT 3: SITE COMPARATOR")
print("=" * 60)

# Process multiple boreholes and compare
bh01_data = ([1.5, 3.0, 6.0, 9.0, 12.0], [5, 8, 18, 35, 60],
             ["Fill", "Sand", "Sand", "Gravel", "Bedrock"], 3.2)
bh02_data = ([1.5, 3.0, 6.0, 9.0, 12.0], [3, 6, 15, 28, 55],
             ["Fill", "Clay", "Sand", "Gravel", "Bedrock"], 2.8)

_, sum1 = process_borehole(*bh01_data, bh_id="BH-01")
_, sum2 = process_borehole(*bh02_data, bh_id="BH-02")

compare = lambda s1, s2, key: f"{s1[key]} vs {s2[key]}"

print(f"  {'Metric':<15} {'BH-01':>8} {'BH-02':>8} {'Better':>8}")
print("  " + "─" * 42)
for key, label in [("avg_n", "Avg N"), ("avg_vs", "Avg Vs"), 
                    ("site_class", "Site Class"), ("weak_layers", "Weak layers")]:
    v1, v2 = sum1[key], sum2[key]
    if isinstance(v1, (int, float)):
        better = "BH-01" if v1 > v2 else "BH-02" if v2 > v1 else "Tie"
    else:
        better = "—"
    print(f"  {label:<15} {str(v1):>8} {str(v2):>8} {better:>8}")

print("\n" + "=" * 60)
print("  Day 007 Complete!")
print("=" * 60)
