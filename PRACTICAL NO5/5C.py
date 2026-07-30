# Practical No. 5 (5c)
# Name : Preethi Naresh
# Roll No : S103

import pandas as pd

print("=" * 40)
print("PRACTICAL NO. 5 (5c)")
print("=" * 40)
print("Name     : Preethi Naresh ")
print("Roll No. : S103 ")
print()

# Create a dictionary
student = {
    "Amit": 85,
    "Neha": 92,
    "Rahul": 78,
    "Priya": 88,
    "Karan": 95
}

# Create Pandas Series from dictionary
series = pd.Series(student)

print("Dictionary:")
print(student)

print("\nPandas Series:")
print(series)
