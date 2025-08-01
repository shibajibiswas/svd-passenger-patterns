import numpy as np
import pandas as pd

# Step 1: Input booking data
# Rows = Passengers (P1 to P5)
# Columns = Features [F1: Weekday Trips, F2: Weekend Trips, F3: Premium Upgrades]
A = np.array([
    [5, 1, 0],   # P1
    [4, 1, 0],   # P2
    [1, 4, 0],   # P3
    [0, 5, 0],   # P4
    [0, 2, 5]    # P5
])

# Step 2: Apply SVD
U, S, VT = np.linalg.svd(A, full_matrices=False)

# Step 3: Reconstruct Σ (Sigma) as a diagonal matrix
Sigma = np.diag(S)

# Optional: Convert results into DataFrames for better readability
df_A = pd.DataFrame(A, columns=["Weekday Trips", "Weekend Trips", "Premium Upgrades"],
                    index=[f"P{i}" for i in range(1, 6)])
df_U = pd.DataFrame(U, columns=[f"U{i}" for i in range(1, U.shape[1]+1)], index=df_A.index)
df_Sigma = pd.DataFrame(Sigma, index=[f"U{i}" for i in range(1, Sigma.shape[0]+1)],
                        columns=[f"Sigma{i}" for i in range(1, Sigma.shape[1]+1)])
df_VT = pd.DataFrame(VT, index=[f"VT{i}" for i in range(1, VT.shape[0]+1)],
                     columns=df_A.columns)

# View intermediate components
print("Original Matrix A:")
print(df_A)

print("\nLeft Singular Vectors (U):")
print(df_U)

print("\nSingular Values (Σ):")
print(df_Sigma)

print("\nRight Singular Vectors Transpose (Vᵀ):")
print(df_VT)
