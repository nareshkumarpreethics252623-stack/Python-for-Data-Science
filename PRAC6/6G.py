import matplotlib.pyplot as plt

# Data
categories = ["Data Structures", "Scala for DS", "Operating System", "Python for DS"]
scores = [65, 70, 74, 60]

explode = (0, 0, 0, 0.1)

# Create pie chart
plt.pie(
    scores,
    labels=categories,
    autopct='%1.1f%%',
    explode=explode,
    startangle=90
)

# Add title
plt.title("Student Scores")

# Display as a circle
plt.axis('equal')

# Show the chart
plt.show()

