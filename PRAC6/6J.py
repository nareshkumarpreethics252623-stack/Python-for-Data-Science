import matplotlib.pyplot as plt

# Data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales_2023 = [150, 200, 250, 300, 280, 350]
sales_2024 = [180, 220, 270, 320, 300, 400]

# Create the plot
plt.figure(figsize=(8, 5))

# Plot sales for 2023
plt.plot(
    months,
    sales_2023,
    color="blue",
    linestyle="--",
    marker="o",
    label="Sales 2023"
)

# Plot sales for 2024
plt.plot(
    months,
    sales_2024,
    color="green",
    linestyle="-",
    marker="s",
    label="Sales 2024"
)

# Add title and labels
plt.title("Monthly Sales Comparison (2023 vs 2024)")
plt.xlabel("Months")
plt.ylabel("Sales")

# Add legend
plt.legend()

# Highlight the highest sales month of 2024
max_sales = max(sales_2024)
max_index = sales_2024.index(max_sales)

plt.annotate(
    f"Highest Sales: {max_sales}",
    xy=(months[max_index], max_sales),
    xytext=(months[max_index], max_sales + 20),
    arrowprops=dict(facecolor="black", arrowstyle="->")
)

# Add grid (optional)
plt.grid(True)

# Save the figure
plt.savefig("sales_comparison.png")

# Display the plot
plt.show()
