import sympy as sp

# Define the variable
n = sp.symbols('n')

# Construct the two parts of the expression
part1 = n * (n + 1) / 2
part2 = (n + 1) * ((n + 1) + 1) / 2

# Combine the parts
expression = part1 + part2

# Expand the expression
expanded_expression = sp.expand(expression)

# Display the expanded expression
print("Expanded Expression:", expanded_expression)

# Factor the expanded expression
factored_expression = sp.factor(expanded_expression)

# Display the factored expression
print("Factored Expression:", factored_expression)
