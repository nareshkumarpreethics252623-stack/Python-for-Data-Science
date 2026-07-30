# Practical No. 5 (5d)
# Name : Preethi Naresh
# Roll No : S103

import pandas as pd

print("=" * 40)
print("PRACTICAL NO. 5 (5d)")
print("=" * 40)
print("Name     : Preethi Naresh")
print("Roll No. : S103 ")
print()

# Create a Pandas Series
marks = pd.Series([45, 68, 72, 55, 89, 91, 60])

print("Original Series:")
print(marks)

# Create a Boolean array
boolean_array = marks >= 70

print("\nBoolean Array:")
print(boolean_array)

# Filter the Series using the Boolean array
filtered_marks = marks[boolean_array]

print("\nFiltered Series (Marks >= 70):")
print(filtered_marks)
