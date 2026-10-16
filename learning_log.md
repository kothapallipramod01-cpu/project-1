# Day 1 Learning Log

## Practised

- Python dictionaries for named descriptor fields.
- Lists and nested loops to build one row per molecule.
- NumPy arrays and 2D matrix shape.
- Indexing: `X[1, :]`, `X[:, 1]`, and `X[:, 0]`.
- Aggregation with `np.mean`.
- Vectorized comparisons and Boolean reduction with `.all()`.
- Conditional logic using `if`, `else`, and `and`.

## Mistakes observed and corrections

### 1. Confused row selection with column selection

**Attempt:** `X[:, 1]` to select the second molecule.  
**Why it was wrong:** The colon before the comma selects all rows. Index `1` after the comma selects the second column.  
**Correction:** `X[1, :]` selects the second row and all columns.  
**My explanation after feedback:** “It takes every element in the second column and it takes every element in the second row.” This correctly captured the distinction after review.

### 2. Used inconsistent variable names in a loop

**Attempt:**
```python
for molecular_rows in molecules:
    print(molecular_row >= 0)
```
**Why it was wrong:** `molecular_rows` and `molecular_row` are different identifiers. The loop may reference an undefined or stale variable.  
**Correction:**
```python
for molecular_row in molecules:
    print(molecular_row >= 0)
```

### 3. Compared a descriptor list to the number 5

**Attempt:**
```python
if feature_matrix == 5:
    print(correct)
```
**Why it was wrong:** It does not check the matrix's number of columns, and `correct` was not defined.  
**Correction:** `X.shape[1] == 5` checks the descriptor count. `X.shape == (3, 5)` checks exact dimensions. Print a string such as `print("Valid")`.

### 4. Reused the matrix name inside a loop

**Attempt:** `for molecules in molecules:`  
**Why it is risky:** It reuses the name for the whole matrix and for each row, which makes code harder to reason about.  
**Correction:** `for molecule_row in X:`.

### 5. Applied a non-negative rule to every descriptor

**Attempt:** `(molecular_row >= 0).all()` for all feature values.  
**Why it was scientifically wrong:** LogP can be negative. One generic rule can reject chemically valid values.  
**Correction:** Use a domain-appropriate rule for each descriptor. This example checks only if molecular weights are positive.

### 6. Treated basic checks as full validation

**Learning point:** Correct dimensions and positive molecular weights do not prove that a molecule's structure or descriptor values are correct.

## Strengths demonstrated

- Built a feature matrix with nested loops.
- Explained the difference between row and column selection after correction.
- Used vectorized comparisons and `.all()`.
- Combined conditions with `if/else` and `and`.

## Weaknesses to practise

These are observed gaps from this session, not a general judgement of ability.

1. **Indexing precision:** identify the row and column before writing an expression.
2. **Variable consistency:** keep loop-variable spelling consistent and avoid shadowing the matrix name.
3. **Debugging:** confirm a name exists and that the operation matches its type.
4. **Shape reasoning:** `.shape[0]` is rows; `.shape[1]` is columns.
5. **Validation design:** each descriptor needs a suitable rule.
6. **Scientific interpretation:** state exactly what a check proves—and what it does not.
   

## Extra NumPy topics needed next

- `ndim`, `size`, `dtype`, and array creation.
- Slicing and Boolean masks.
- `np.any`, `np.all`, `np.isfinite`, and `np.isnan`.
- `axis=0` and `axis=1` for reductions.
- Broadcasting and shape compatibility.
- Reshaping, stacking, missing-value handling, assertions, tests, and reproducibility.

## Reflection

Add your own explanations after answering the understanding check.

- What did I understand best?
- What still requires effort?
- Which error can I now prevent?
- What test would catch the error in the future?
