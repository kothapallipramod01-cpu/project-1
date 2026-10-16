"""Day 1: toy molecular descriptor matrix.

These values are illustrative programming data, not validated chemistry.
Do not use them for scientific inference or model training.
"""
import numpy as np

molecule_1 = {
    "name": "paracetamol",
    "molecular_weight": 250,  # Toy value; inaccurate
    "logp": 3.5,
    "hbd": 0.4,
    "hba": 8,
    "tpsa": 1.6,
}
molecule_2 = {
    "name": "ibuprofen",
    "molecular_weight": 43,  # Toy value; inaccurate
    "logp": 20,
    "hbd": 9,
    "hba": 3.2,
    "tpsa": 7.9,
}
molecule_3 = {
    "name": "dogiperol",  # Unverified label for the exercise
    "molecular_weight": 20,
    "logp": 1,
    "hbd": 0.5,
    "hba": 2.3,
    "tpsa": 3.4,
}

molecules_alpha = [molecule_1, molecule_2, molecule_3]
feature_descriptors = [
    "molecular_weight",
    "logp",
    "hbd",
    "hba",
    "tpsa",
]

feature_rows = []
for molecule in molecules_alpha:
    row = []
    for feature in feature_descriptors:
        row.append(molecule[feature])
    feature_rows.append(row)

X = np.array(feature_rows, dtype=float)

print("Feature matrix:")
print(X)
print("Shape:", X.shape)  # Expected: (3, 5)

# X[row, column]; indexes start at zero.
print("Second molecule, all descriptors:", X[1, :])
print("LogP for all molecules:", X[:, 1])
print("Mean molecular weight:", np.mean(X[:, 0]))

all_molecular_weights_positive = (X[:, 0] > 0).all()

# These are basic checks, not full chemical validation.
if X.shape == (3, 5) and all_molecular_weights_positive:
    print("Dataset passed basic checks")
else:
    print("Dataset failed basic checks")

print("All values finite:", np.isfinite(X).all())

# A distinct loop variable avoids overwriting the matrix name.
for molecule_row in X:
    print("Row:", molecule_row)
