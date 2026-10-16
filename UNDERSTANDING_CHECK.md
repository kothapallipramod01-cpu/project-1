# Day 1 — Understanding Check

Answer in your own words. Code can support your answer, but do not only paste code. If unsure, write your best attempt and state what confuses you.

## Core questions

1. If `X.shape == (3, 5)`, what does each number mean in this project?
2. Explain the difference between `X[1, :]` and `X[:, 1]`. What does each return?
3. Why does index `1` select the second row or column?
4. What does `X[:, 0] > 0` return? Why do we add `.all()`?
5. Explain this condition:
   ```python
   if X.shape == (3, 5) and (X[:, 0] > 0).all():
       print("Dataset passed basic checks")
   ```
6. Does passing the condition prove that the molecules are chemically valid? Why?
7. Why is it unsafe to require every descriptor to be non-negative? Give an example from this project.
8. What can go wrong with `for molecules in molecules:`?
9. What is the difference between a list of dictionaries and a 2D NumPy array?
10. Why should descriptor names and their order be stored explicitly?

## Transfer exercises

Assume `X` is a 3-by-5 matrix with columns in this order: molecular weight, LogP, HBD, HBA, TPSA.

11. Select all descriptors for the third molecule.
12. Select HBA values for all molecules.
13. Calculate the mean molecular weight.
14. Check for exactly three rows and five columns.
15. Check whether all molecular weights are positive.
16. Check whether all numeric values are finite.

## Scientific reasoning

17. A matrix has the correct shape, but one record came from an invalid SMILES string. Why is shape validation not enough? Name one additional validation step.

## Self-rating

Rate each topic: 0 = cannot explain yet; 1 = can explain with a hint; 2 = can explain and solve a new example independently.

- Row/column indexing
- Shape
- Vectorized comparison
- `.all()`
- Loops and variable naming
- Scientific validation

## After review

For every incorrect answer, record: what was wrong, why it was wrong, the correction, and a new example you can solve independently.
