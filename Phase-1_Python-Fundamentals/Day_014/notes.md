# Day 014: Regular Expressions

## Phase: Python Fundamentals

**Date:** YYYY-MM-DD  
**Time Spent:** ~60 minutes

---

## Concepts Covered

- The `re` module — `re.search()`, `re.findall()`, `re.match()`, `re.sub()`, `re.split()`
- Basic patterns: literal characters, character classes (`\d`, `\w`, `\s`), quantifiers (`+`, `*`, `?`, `{n,m}`)
- Groups and named groups for extracting structured data from text
- Anchors (`^`, `$`) and word boundaries (`\b`)
- Compiling patterns with `re.compile()` for repeated use
- Parsing unstructured borehole log text to extract depths, N-values, and soil descriptions
- Using `re.sub()` to clean and normalize messy field data

## Key Takeaways

1. **Regex turns unstructured text into structured data.** Borehole logs from older projects often arrive as plain text or scanned PDFs. A pattern like `r'(\d+\.?\d*)\s*m.*?N\s*=\s*(\d+)'` can extract depth-N pairs from free-form descriptions that would be painful to parse with `.split()` alone.
2. **Named groups make extraction self-documenting.** `r'(?P<depth>\d+\.?\d*)\s*m'` returns matches you access as `match['depth']` instead of `match.group(1)` — clearer code when parsing complex field logs with multiple data fields per line.
3. **`re.sub()` is essential for data cleaning.** Replacing inconsistent units, stripping non-numeric characters from N-values, or normalizing soil descriptions before classification — all common preprocessing steps before data enters an ML pipeline.

## Code Summary

- Parsed a multi-line borehole log text to extract depth, N-value, and soil description from each entry using `re.findall()` with a grouped pattern
- Extracted all SPT N-values from a free-form site investigation summary using `re.findall(r'N\s*=\s*(\d+)', text)`
- Used named groups to parse structured test result strings into dictionaries
- Cleaned messy field data with `re.sub()` — removed non-numeric characters, standardized unit labels, normalized whitespace
- Split complex soil descriptions into components using `re.split()` on multiple delimiters
- Compiled frequently used patterns with `re.compile()` for efficient repeated matching

## Geotechnical Application

- **Parsing legacy borehole logs:** extracting depth, blow count, and soil type from plain-text or digitized borehole records that lack consistent formatting
- **Extracting N-values from reports:** scanning site investigation text summaries to pull all SPT results into a structured dataset for analysis
- **Data cleaning before ML:** normalizing soil descriptions (e.g., mapping varied text representations to a single canonical form), stripping footnotes and annotations from numeric fields
- **Validating input formats:** checking that borehole IDs follow a consistent pattern (`BH-\d{2}`), depths are in expected format, and lab test results match expected structure

## Resources

- [Python `re` Module Documentation](https://docs.python.org/3/library/re.html)
- [Regular Expressions 101 — Online Tester](https://regex101.com/)
- [Real Python — Regular Expressions in Python](https://realpython.com/regex-python/)

---

> *Day 014 of 100 — 100 Days of ML for Geotechnical Engineering*
