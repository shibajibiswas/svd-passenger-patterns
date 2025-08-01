# svd-passenger-patterns
Discover Hidden Passenger Patterns using SVD. This repo demonstrates how Singular Value Decomposition (SVD) can reveal behavioral clusters in train booking data using a simple Python+NumPy example.


# 🚆 SVD Passenger Patterns: Discover Hidden Behaviors in Train Booking Data

This repository contains example Python code accompanying the Medium blog post  
**“Singular Value Decomposition: The Swiss Army Knife of Data Reduction”**  
[Read the blog here →](https://medium.com/@your-medium-handle) 

---

## 🧠 What is this about?

We explore **Singular Value Decomposition (SVD)** in a storytelling format using a fictional train booking dataset.

- Rows = Passengers  
- Columns = Booking behavior features like Weekday Trips, Weekend Trips, and Premium Upgrades  
- SVD helps us **discover latent behavioral patterns** (e.g., Weekend Adventurers, Premium Loyalists)

---

## 🔍 Use Case

Railways or travel systems often deal with high-dimensional booking data.  
Using SVD, we can:
- Reduce dimensions while keeping the story intact
- Discover dominant passenger segments
- Optimize pipeline/storage by prioritizing top singular values

---

## 📦 Files

| File | Description |
|------|-------------|
| `svd_analysis.py` | Clean NumPy-based script performing SVD on a toy dataset |
| `svd_analysis.ipynb` | *(optional)* Jupyter Notebook version with inline commentary |
| `README.md` | This file |

---

## 🧪 Sample Output

```python
Original Matrix A:
     Weekday Trips  Weekend Trips  Premium Upgrades
P1               5              1                 0
P2               4              1                 0
P3               1              4                 0
P4               0              5                 0
P5               0              2                 5

Top Patterns Discovered (from Σ):
→ Pattern 1: Premium-class loyalists
→ Pattern 2: Weekend adventurers
