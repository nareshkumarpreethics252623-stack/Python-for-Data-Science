import matplotlib.pyplot as plt
import numpy as np

# Data for line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Data for bar chart
categories = ["Data Structures", "Scala for DS", "Operating System", "Python for DS"]
scores = [65, 70, 74, 60]

# Data for scatter plot
x_scatter = [5, 7, 8, 7, 6, 9, 5]
y_scatter = [99, 86, 87, 88, 100, 86, 103]

# Data for histogram
data = np.random.randn(100)

# Create a 2x2 grid of subplots
plt.figure(figsize=(10, 8))

# Top-left: Line Plot
plt.subplot(2, 2, 1)
plt.plot(x, y, marker='o')
plt.title("Line Plot")
plt.xlabel("Numbers")
plt.ylabel("Doubles")

# Top-right: Bar Chart
plt.subplot(2, 2, 2)
plt.bar(categories, scores)
plt.title("Bar Chart")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.xticks(rotation=15)

# Bottom-left: Scatter Plot
plt.subplot(2, 2, 3)
plt.scatter(x_scatter, y_scatter, color='green', s=100)
plt.title("Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Bottom-right: Histogram
plt.subplot(2, 2, 4)
plt.hist(data, bins=20)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)

# Adjust layout
plt.tight_layout()

# Display the figure
plt.show()
