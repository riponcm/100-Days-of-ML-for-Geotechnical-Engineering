"""
Day 006: Dictionaries & Comprehensions
100 Days of ML for Geotechnical Engineering
Phase: Python Fundamentals

Author: Ripon Chandra Malo
Date: February 21, 2026

Geotechnical Problem: Structured Borehole Records & Multi-Borehole Lookup
──────────────────────────────────────────────────────────────────────────
Until now, our borehole data lived in PARALLEL LISTS:
    depths     = [1.5, 3.0, 4.5, ...]
    n_values   = [5,   8,   12,  ...]
    soil_types = ["Fill", "Sand", ...]

Problem: If you want Layer 4's data, you need to know that index 3
means the same thing across ALL lists. One wrong index = wrong data.

A DICTIONARY solves this by using LABELS instead of positions:
    layer = {"depth": 6.0, "N60": 18, "soil": "Clayey Sand", "Vs": 240.4}

Now you access data by NAME: layer["N60"] — no index guessing.

Today we learn dictionaries — the Python structure that mirrors
how engineers actually think about data: labeled records with
named fields.
"""

# ══════════════════════════════════════════════════════════════
# PART 1: CREATING DICTIONARIES — Key-Value Pairs
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 1: CREATING DICTIONARIES")
print("=" * 60)

# A dictionary maps KEYS to VALUES
# Syntax: {key: value, key: value, ...}

# One SPT layer as a dictionary
layer = {
    "depth": 6.0,
    "N60": 18,
    "soil": "Clayey Sand",
    "USCS": "SC",
    "saturated": True,
    "color": "grey"
}

print("Layer dictionary:")
print(layer)
print(f"Type: {type(layer)}")
print(f"Number of entries: {len(layer)}")
print()

# Compare to the old way (parallel lists):
# To get N60 of layer 4, you'd do: n_values[3]   ← what does 3 mean?
# With a dictionary: layer["N60"]                 ← crystal clear!

# Access values by key name
print(f"Depth: {layer['depth']}m")
print(f"N60:   {layer['N60']}")
print(f"Soil:  {layer['soil']}")
print(f"Sat:   {layer['saturated']}")
print()

# Keys can be strings, numbers, or tuples (anything immutable)
# Values can be ANYTHING: strings, numbers, lists, even other dicts

# Empty dictionary
empty_record = {}
print(f"Empty dict: {empty_record}")
print()


# ══════════════════════════════════════════════════════════════
# PART 2: ACCESSING VALUES — Multiple Ways
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 2: ACCESSING VALUES")
print("=" * 60)

layer = {"depth": 6.0, "N60": 18, "soil": "Clayey Sand", "Vs": 240.4}

# Method 1: Square brackets (raises KeyError if key missing)
print(f"layer['N60'] = {layer['N60']}")
print()

# Method 2: .get() — returns None (or default) if key missing
print(f"layer.get('N60')      = {layer.get('N60')}")
print(f"layer.get('color')    = {layer.get('color')}")         # None
print(f"layer.get('color', 'unknown') = {layer.get('color', 'unknown')}")  # default
print()

# WHY .get() matters:
# layer['color']           ← KeyError! Program crashes.
# layer.get('color', '-')  ← Returns '-'. Program continues.
# In real data, fields are often missing. .get() handles this safely.

# Method 3: Check if key exists with 'in'
print(f"'N60' in layer:   {'N60' in layer}")
print(f"'color' in layer: {'color' in layer}")
print()


# ══════════════════════════════════════════════════════════════
# PART 3: MODIFYING DICTIONARIES — Add, Update, Delete
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 3: MODIFYING DICTIONARIES")
print("=" * 60)

layer = {"depth": 6.0, "N60": 18, "soil": "Clayey Sand"}
print(f"Original: {layer}")

# ADD a new key-value pair
layer["Vs"] = 240.4
layer["saturated"] = True
print(f"After add: {layer}")

# UPDATE an existing value
layer["N60"] = 20  # Corrected field reading
print(f"After update N60: {layer}")

# DELETE a key-value pair
del layer["saturated"]
print(f"After del: {layer}")

# pop() — remove AND return the value
vs = layer.pop("Vs")
print(f"Popped Vs={vs}: {layer}")
print()

# UPDATE multiple keys at once with .update()
layer.update({"Vs": 245.0, "Dr": 65.0, "color": "grey"})
print(f"After .update(): {layer}")
print()


# ══════════════════════════════════════════════════════════════
# PART 4: DICTIONARY METHODS — Keys, Values, Items
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 4: KEYS, VALUES, ITEMS")
print("=" * 60)

layer = {
    "depth": 6.0,
    "N60": 18,
    "soil": "Clayey Sand",
    "Vs": 240.4,
    "Dr": 65.0
}

# .keys() — all key names
print(f"Keys:   {list(layer.keys())}")

# .values() — all values
print(f"Values: {list(layer.values())}")

# .items() — all key-value pairs as tuples
print(f"Items:  {list(layer.items())}")
print()

# Most common use: looping through items
print("Loop through key-value pairs:")
for key, value in layer.items():
    print(f"  {key:8s} → {value}")
print()

# Loop through keys only
print("Loop through keys:")
for key in layer:           # or: for key in layer.keys()
    print(f"  {key}: {layer[key]}")
print()


# ══════════════════════════════════════════════════════════════
# PART 5: NESTED DICTIONARIES — Complex Borehole Records
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 5: NESTED DICTIONARIES")
print("=" * 60)

# A single borehole with all its data
borehole = {
    "id": "BH-01",
    "location": {
        "latitude": 40.7608,
        "longitude": -111.8910,
        "elevation": 1320.5,
        "city": "Salt Lake City"
    },
    "water_table": 3.2,
    "date": "2026-02-19",
    "layers": [
        {"depth": 1.5, "N60": 5,  "soil": "Fill"},
        {"depth": 3.0, "N60": 8,  "soil": "Silty Sand"},
        {"depth": 4.5, "N60": 12, "soil": "Sand"},
        {"depth": 6.0, "N60": 18, "soil": "Clayey Sand"},
        {"depth": 7.5, "N60": 28, "soil": "Sand"},
    ]
}

# Access nested data with chained keys
print(f"Borehole: {borehole['id']}")
print(f"City: {borehole['location']['city']}")
print(f"Lat:  {borehole['location']['latitude']}")
print(f"WT:   {borehole['water_table']}m")
print(f"Number of layers: {len(borehole['layers'])}")
print()

# Access a specific layer
layer_3 = borehole["layers"][2]  # 3rd layer (index 2)
print(f"Layer 3: {layer_3}")
print(f"Layer 3 soil: {layer_3['soil']}")
print(f"Layer 3 N60:  {layer_3['N60']}")
print()

# Loop through all layers
print("All layers:")
for i, layer in enumerate(borehole["layers"], start=1):
    print(f"  Layer {i}: {layer['depth']}m | N={layer['N60']:3d} | {layer['soil']}")
print()


# ══════════════════════════════════════════════════════════════
# PART 6: LIST OF DICTIONARIES — The Most Common Data Pattern
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 6: LIST OF DICTIONARIES")
print("=" * 60)

# This is the pattern you'll use most often in data science.
# Each dictionary is a ROW. The list is the TABLE.
# This is exactly how Pandas DataFrames work internally.

layers = [
    {"depth": 1.5,  "N60": 5,  "soil": "Fill",          "color": "dark brown"},
    {"depth": 3.0,  "N60": 8,  "soil": "Silty Sand",    "color": "grey-brown"},
    {"depth": 4.5,  "N60": 12, "soil": "Sand",           "color": "tan"},
    {"depth": 6.0,  "N60": 18, "soil": "Clayey Sand",    "color": "grey"},
    {"depth": 7.5,  "N60": 28, "soil": "Sand",           "color": "brown"},
    {"depth": 9.0,  "N60": 35, "soil": "Gravel",         "color": "grey"},
    {"depth": 10.5, "N60": 50, "soil": "Weathered Rock",  "color": "grey"},
    {"depth": 12.0, "N60": 60, "soil": "Bedrock",         "color": "grey"},
]

# Access by name — so much clearer than parallel lists!
print(f"Layer 4 depth: {layers[3]['depth']}m")
print(f"Layer 4 N60:   {layers[3]['N60']}")
print(f"Layer 4 soil:  {layers[3]['soil']}")
print()

# Extract a column (list comprehension)
all_n = [layer["N60"] for layer in layers]
all_depths = [layer["depth"] for layer in layers]
print(f"All N60:    {all_n}")
print(f"All depths: {all_depths}")
print()

# Filter rows
sandy = [l for l in layers if "Sand" in l["soil"]]
print(f"Sandy layers ({len(sandy)}):")
for s in sandy:
    print(f"  {s['depth']}m | N={s['N60']} | {s['soil']}")
print()

# Print a table
print(f"  {'#':>2} {'Depth':>6} {'N60':>4} {'Soil':16s} {'Color':12s}")
print("  " + "─" * 44)
for i, l in enumerate(layers, start=1):
    print(f"  {i:2d} {l['depth']:5.1f}m {l['N60']:4d} {l['soil']:16s} {l['color']:12s}")
print()


# ══════════════════════════════════════════════════════════════
# PART 7: DICTIONARY AS LOOKUP TABLE — Instant Access by Key
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 7: DICTIONARY AS LOOKUP TABLE")
print("=" * 60)

# Instead of searching a list, look up directly by key.
# This is like a phone book: you look up a name, get the number.

# Soil classification lookup
soil_unit_weight = {
    "Fill": 16.0,
    "Sand": 18.5,
    "Silty Sand": 17.5,
    "Clayey Sand": 18.0,
    "Clay": 17.0,
    "Gravel": 20.0,
    "Weathered Rock": 22.0,
    "Bedrock": 25.0,
}

# Instant lookup — no searching!
print(f"Unit weight of Sand:    {soil_unit_weight['Sand']} kN/m³")
print(f"Unit weight of Gravel:  {soil_unit_weight['Gravel']} kN/m³")
print(f"Unit weight of Bedrock: {soil_unit_weight['Bedrock']} kN/m³")
print()

# Use in calculations
for l in layers[:4]:
    gamma = soil_unit_weight.get(l["soil"], 18.0)  # default 18 if not found
    sigma_v = gamma * l["depth"]
    print(f"  {l['depth']:4.1f}m | {l['soil']:16s} | γ={gamma:5.1f} | σv={sigma_v:6.1f} kN/m²")
print()

# USCS classification lookup
uscs_description = {
    "GW": "Well-graded Gravel",
    "GP": "Poorly-graded Gravel",
    "SW": "Well-graded Sand",
    "SP": "Poorly-graded Sand",
    "SM": "Silty Sand",
    "SC": "Clayey Sand",
    "ML": "Low-plasticity Silt",
    "CL": "Low-plasticity Clay",
    "CH": "High-plasticity Clay",
    "OH": "Organic Clay",
    "PT": "Peat",
}

test_codes = ["SM", "CL", "SW", "XX"]
print("USCS Lookup:")
for code in test_codes:
    desc = uscs_description.get(code, "Unknown classification")
    print(f"  {code} → {desc}")
print()


# ══════════════════════════════════════════════════════════════
# PART 8: MULTI-BOREHOLE DATABASE — Dictionary of Dictionaries
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 8: MULTI-BOREHOLE DATABASE")
print("=" * 60)

# Key = borehole ID, Value = borehole data dictionary
# This is a simple database — look up any borehole by name.

site_database = {
    "BH-01": {
        "location": (40.7608, -111.8910),
        "wt": 3.2,
        "layers": [
            {"depth": 1.5, "N60": 5, "soil": "Fill"},
            {"depth": 3.0, "N60": 8, "soil": "Silty Sand"},
            {"depth": 6.0, "N60": 18, "soil": "Sand"},
            {"depth": 9.0, "N60": 35, "soil": "Gravel"},
            {"depth": 12.0, "N60": 60, "soil": "Bedrock"},
        ]
    },
    "BH-02": {
        "location": (40.7615, -111.8895),
        "wt": 2.8,
        "layers": [
            {"depth": 1.5, "N60": 3, "soil": "Fill"},
            {"depth": 3.0, "N60": 6, "soil": "Clay"},
            {"depth": 6.0, "N60": 15, "soil": "Sand"},
            {"depth": 9.0, "N60": 28, "soil": "Gravel"},
            {"depth": 12.0, "N60": 55, "soil": "Bedrock"},
        ]
    },
    "BH-03": {
        "location": (40.7602, -111.8920),
        "wt": 4.0,
        "layers": [
            {"depth": 1.5, "N60": 7, "soil": "Fill"},
            {"depth": 3.0, "N60": 12, "soil": "Sand"},
            {"depth": 6.0, "N60": 25, "soil": "Sand"},
            {"depth": 9.0, "N60": 40, "soil": "Gravel"},
            {"depth": 12.0, "N60": 65, "soil": "Bedrock"},
        ]
    }
}

# Instant access to any borehole
bh = site_database["BH-02"]
print(f"BH-02 water table: {bh['wt']}m")
print(f"BH-02 location:    {bh['location']}")
print(f"BH-02 layer 3:     {bh['layers'][2]}")
print()

# Loop through all boreholes
print("Site Summary:")
for bh_id, data in site_database.items():
    n_vals = [l["N60"] for l in data["layers"]]
    avg_n = sum(n_vals) / len(n_vals)
    print(f"  {bh_id}: WT={data['wt']}m | Avg N={avg_n:.1f} | "
          f"Layers={len(data['layers'])}")
print()


# ══════════════════════════════════════════════════════════════
# PART 9: DICTIONARY COMPREHENSION — One-Line Dict Creation
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 9: DICTIONARY COMPREHENSION")
print("=" * 60)

# Just like list comprehension, but creates a dictionary.
# Syntax: {key_expr: value_expr FOR variable IN iterable}

n_values = [5, 8, 12, 18, 28, 35, 50, 60]
depths = [1.5, 3.0, 4.5, 6.0, 7.5, 9.0, 10.5, 12.0]

# Create a depth → N60 lookup
depth_to_n = {d: n for d, n in zip(depths, n_values)}
print(f"Depth → N60 lookup: {depth_to_n}")
print(f"  N60 at 6.0m: {depth_to_n[6.0]}")
print()

# Vs for each depth
depth_to_vs = {d: round(97 * (n ** 0.314), 1)
               for d, n in zip(depths, n_values)}
print(f"Depth → Vs: {depth_to_vs}")
print()

# Classification lookup
n_to_class = {n: ("Dense+" if n >= 30 else "Med" if n >= 10 else "Loose")
              for n in n_values}
print(f"N → Class: {n_to_class}")
print()

# With filter — only saturated layers
wt = 3.2
sat_layers = {d: n for d, n in zip(depths, n_values) if d > wt}
print(f"Saturated (d>{wt}m): {sat_layers}")
print()

# From a list of dicts — build lookup by soil type
layers = [
    {"depth": 1.5, "N60": 5, "soil": "Fill"},
    {"depth": 3.0, "N60": 8, "soil": "Silty Sand"},
    {"depth": 6.0, "N60": 18, "soil": "Sand"},
]
soil_lookup = {l["soil"]: l["N60"] for l in layers}
print(f"Soil → N60: {soil_lookup}")
print()


# ══════════════════════════════════════════════════════════════
# PART 10: COUNTING & GROUPING — Common Data Operations
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  PART 10: COUNTING & GROUPING")
print("=" * 60)

# Count occurrences of each soil type
all_soils = ["Fill", "Sand", "Clay", "Sand", "Gravel",
             "Sand", "Clay", "Sand", "Bedrock"]

# Manual counting with dictionary
soil_count = {}
for soil in all_soils:
    if soil in soil_count:
        soil_count[soil] += 1
    else:
        soil_count[soil] = 1

print(f"Soil counts (manual): {soil_count}")

# Cleaner with .get()
soil_count2 = {}
for soil in all_soils:
    soil_count2[soil] = soil_count2.get(soil, 0) + 1
print(f"Soil counts (.get()): {soil_count2}")
print()

# Group layers by consistency class
layers_full = [
    {"depth": 1.5, "N60": 5, "soil": "Fill"},
    {"depth": 3.0, "N60": 8, "soil": "Sand"},
    {"depth": 4.5, "N60": 12, "soil": "Sand"},
    {"depth": 6.0, "N60": 18, "soil": "Clay"},
    {"depth": 7.5, "N60": 28, "soil": "Sand"},
    {"depth": 9.0, "N60": 35, "soil": "Gravel"},
    {"depth": 10.5, "N60": 50, "soil": "Rock"},
    {"depth": 12.0, "N60": 60, "soil": "Bedrock"},
]

def classify(n):
    if n < 10: return "Loose"
    elif n < 30: return "Medium Dense"
    elif n < 50: return "Dense"
    else: return "Very Dense"

groups = {}
for layer in layers_full:
    cls = classify(layer["N60"])
    if cls not in groups:
        groups[cls] = []
    groups[cls].append(layer["depth"])

print("Layers grouped by consistency:")
for cls, deps in groups.items():
    print(f"  {cls:13s}: depths = {deps}")
print()


# ══════════════════════════════════════════════════════════════
# PART 11: COMPLETE APPLICATION — Site Investigation Report
# ══════════════════════════════════════════════════════════════

print("=" * 60)
print("  COMPLETE: SITE INVESTIGATION REPORT")
print("=" * 60)

# Full site data as structured dictionaries
site = {
    "project": "Highway Bridge Foundation",
    "location": "Salt Lake City, Utah",
    "coordinates": (40.7608, -111.8910),
    "date": "2026-02-19",
    "boreholes": {
        "BH-01": {
            "wt": 3.2,
            "layers": [
                {"depth": 1.5,  "N60": 5,  "soil": "Fill"},
                {"depth": 3.0,  "N60": 8,  "soil": "Silty Sand"},
                {"depth": 4.5,  "N60": 12, "soil": "Sand"},
                {"depth": 6.0,  "N60": 18, "soil": "Clayey Sand"},
                {"depth": 7.5,  "N60": 28, "soil": "Sand"},
                {"depth": 9.0,  "N60": 35, "soil": "Gravel"},
                {"depth": 10.5, "N60": 50, "soil": "Weathered Rock"},
                {"depth": 12.0, "N60": 60, "soil": "Bedrock"},
            ]
        },
        "BH-02": {
            "wt": 2.8,
            "layers": [
                {"depth": 1.5,  "N60": 3,  "soil": "Fill"},
                {"depth": 3.0,  "N60": 6,  "soil": "Clay"},
                {"depth": 4.5,  "N60": 10, "soil": "Sand"},
                {"depth": 6.0,  "N60": 15, "soil": "Clayey Sand"},
                {"depth": 7.5,  "N60": 22, "soil": "Sand"},
                {"depth": 9.0,  "N60": 30, "soil": "Gravel"},
                {"depth": 10.5, "N60": 45, "soil": "Weathered Rock"},
                {"depth": 12.0, "N60": 55, "soil": "Bedrock"},
            ]
        }
    }
}

# Unit weight lookup
gamma_lookup = {
    "Fill": 16.0, "Sand": 18.5, "Silty Sand": 17.5,
    "Clayey Sand": 18.0, "Clay": 17.0, "Gravel": 20.0,
    "Weathered Rock": 22.0, "Bedrock": 25.0,
}

# Report header
lat, lon = site["coordinates"]
print(f"  Project:  {site['project']}")
print(f"  Location: {site['location']} ({lat}, {lon})")
print(f"  Date:     {site['date']}")
print(f"  Boreholes: {list(site['boreholes'].keys())}")
print()

# Process each borehole
for bh_id, bh_data in site["boreholes"].items():
    print(f"  {'═' * 70}")
    print(f"  {bh_id} | Water Table: {bh_data['wt']}m")
    print(f"  {'─' * 70}")
    print(f"  {'#':>3} {'Dep':>5} {'N60':>4} {'Soil':16s} {'Class':13s} {'Vs':>6} {'σv':>7}")
    print(f"  {'─' * 70}")
    
    n_all = []
    vs_all = []
    
    for i, layer in enumerate(bh_data["layers"], start=1):
        d = layer["depth"]
        n = layer["N60"]
        s = layer["soil"]
        
        # Calculations using dictionary lookups
        Vs = 97 * (n ** 0.314)
        gamma = gamma_lookup.get(s, 18.0)
        sigma_v = gamma * d
        
        if n < 4: cons = "Very Loose"
        elif n < 10: cons = "Loose"
        elif n < 30: cons = "Medium Dense"
        elif n < 50: cons = "Dense"
        else: cons = "Very Dense"
        
        n_all.append(n)
        vs_all.append(Vs)
        
        print(f"  {i:3d} {d:4.1f}m {n:4d} {s:16s} {cons:13s} {Vs:5.1f} {sigma_v:6.1f}")
    
    # Summary stats (dict comprehension for per-borehole results)
    avg_n = sum(n_all) / len(n_all)
    avg_vs = sum(vs_all) / len(vs_all)
    weak = len([n for n in n_all if n < 15])
    
    print(f"  {'─' * 70}")
    print(f"  Avg N: {avg_n:.1f} | Avg Vs: {avg_vs:.1f} m/s | Weak layers: {weak}")

# Cross-borehole comparison
print(f"\n  {'═' * 70}")
print("  CROSS-BOREHOLE COMPARISON")
print(f"  {'─' * 70}")

bh_summary = {}
for bh_id, bh_data in site["boreholes"].items():
    n_vals = [l["N60"] for l in bh_data["layers"]]
    soils = set(l["soil"] for l in bh_data["layers"])
    bh_summary[bh_id] = {
        "avg_n": sum(n_vals) / len(n_vals),
        "min_n": min(n_vals),
        "max_n": max(n_vals),
        "unique_soils": soils,
    }

for bh_id, stats in bh_summary.items():
    print(f"  {bh_id}: Avg N={stats['avg_n']:.1f} | "
          f"Range: {stats['min_n']}–{stats['max_n']} | "
          f"Soils: {len(stats['unique_soils'])}")

# Common soils across all boreholes (set intersection)
all_soil_sets = [stats["unique_soils"] for stats in bh_summary.values()]
common_soils = all_soil_sets[0]
for soil_set in all_soil_sets[1:]:
    common_soils = common_soils & soil_set
print(f"  Common soils: {common_soils}")

print("\n" + "=" * 60)
print("  Day 006 Complete!")
print("=" * 60)
