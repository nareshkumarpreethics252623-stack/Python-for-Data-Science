import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

categories = ["Data Structures", "Scala for DS", "Operating System", "Python for DS"]
scores = [65, 70, 74, 60]

# Create a figure with 2 subplots
plt.figure(figsize=(10, 4))

# First subplot: Line Plot
plt.subplot(1, 2, 1)
plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("Numbers")
plt.ylabel("Doubles")

# Second subplot: Bar Chart
plt.subplot(1, 2, 2)
plt.bar(categories, scores)
plt.title("Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.xticks(rotation=15)

# Adjust layout
plt.tight_layout()

# Display the figure
plt.show()
