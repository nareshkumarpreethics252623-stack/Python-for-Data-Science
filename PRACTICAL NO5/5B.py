# Practical No. 5 (5b)
# Name : Preethi Naresh
# Roll No : S103

import pandas as pd

print("=" * 40)
print("PRACTICAL NO. 5 (5b)")
print("=" * 40)
print("Name     : Preethi Naresh")
print("Roll No. : S103")
print()

# Read Excel file
df = pd.read_excel("StressLevelDataset.xlsx")

print("Statistical Information of Dataset")
print()

print(df.describe())
