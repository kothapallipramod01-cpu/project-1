# Project Prometheus — Molecular Data Engine

**Status:** Day 1 learning record  
**Goal:** Build a reproducible pipeline for molecular data representation, validation, descriptors, and features for later machine-learning work.

## Day 1 scope

This checkpoint covers Python dictionaries and loops, building a NumPy feature matrix, reading array shape, row/column indexing, vectorized comparisons, and basic validation.

> **Scientific caution:** The values in this exercise are toy values for programming practice, not verified chemistry. The molecular-weight entries for paracetamol and ibuprofen are inaccurate. The compound label “dogiperol” is unverified. Do not use this matrix for scientific conclusions or model training. Later checkpoints will use molecular structures and RDKit-derived descriptors.

## Files

- `src/day1_feature_matrix.py` — runnable example.
- `learning_log.md` — observed mistakes, corrections, strengths, and learning gaps.
- `UNDERSTANDING_CHECK.md` — questions that test understanding and transfer.

## Requirements and execution

Python 3 and NumPy are required.

```bash
python -m pip install numpy
python src/day1_feature_matrix.py
```

## Main concepts

1. Store named fields in dictionaries.
2. Use an ordered list for descriptor names.
3. Build one feature row per molecule.
4. Convert the rows to a 2D NumPy array.
5. Inspect dimensions with `X.shape`.
6. Select rows and columns with `X[row, column]`.
7. Use vectorized comparisons and `.all()`.
8. Combine conditions with `and`.

## Validation limits

Current checks test the expected shape and positive molecular weights only. They do not prove that structures are chemically valid, descriptor values are correct, or the data are suitable for scientific inference.

## Learning workflow

Write the code yourself, run it, record the actual output, explain mistakes in your own words, answer the understanding check, and commit meaningful changes.
