# Practical No. 5 (5c)
# Name : Your Name
# Roll No : Your Roll No.

import pandas as pd

print("=" * 40)
print("PRACTICAL NO. 5 (5c)")
print("=" * 40)
print("Name     : Your Name")
print("Roll No. : Your Roll No.")
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
