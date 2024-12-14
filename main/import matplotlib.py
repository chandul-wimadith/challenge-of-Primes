import matplotlib.pyplot as plt

# Function to calculate triangular numbers
def triangular(n):
    return n * (n + 1) // 2

# Number of terms to visualize
n_terms = 10

# Generate triangular numbers
triangular_numbers = [triangular(n) for n in range(1, n_terms + 1)]
triangular_plus_one = [num + 1 for num in triangular_numbers]

# Calculate sums of consecutive triangular numbers (which are perfect squares)
sums = [triangular_numbers[n] + triangular_numbers[n + 1] for n in range(n_terms - 1)]
squares = [(n + 1) ** 2 for n in range(1, n_terms)]

# Prepare x values for plotting
x_values_triangular = list(range(1, n_terms + 1))  # x values for triangular numbers
x_values_sums = list(range(1, n_terms))  # x values for sums and squares

# Plotting
plt.figure(figsize=(12, 8))

# Plot triangular numbers
plt.plot(x_values_triangular, triangular_numbers, marker='o', label='Triangular Numbers', color='blue')

# Plot triangular numbers + 1
plt.plot(x_values_triangular, triangular_plus_one, marker='s', label='Triangular Numbers + 1', color='orange')

# Plot sums of consecutive triangular numbers
plt.plot(x_values_sums, sums, marker='^', label='Sum of Consecutive Triangular Numbers', color='green')

# Plot square numbers
plt.plot(x_values_sums, squares, marker='x', label='Square Numbers', color='red')

# Adding labels and title
plt.title('Visualization of Triangular Numbers and Their Relationships')
plt.xlabel('n (Position)')
plt.ylabel('Value')
plt.xticks(range(1, n_terms + 1))
plt.legend()
plt.grid()

# Show the plot
plt.show()