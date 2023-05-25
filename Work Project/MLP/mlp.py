from pulp import LpProblem, LpVariable, LpMinimize

# Create the LP problem
model = LpProblem("TruckSchedulingProblem", LpMinimize)

# Decision Variables
X = LpVariable("X", lowBound=0, cat="Integer")

# Objective Function
model += X

# Constraints
model += 2 * X >= 5
model += 3 * X <= 10

# Solve the problem
model.solve()

# Print the optimal solution
print("Optimal Solution:")
print("X =", X.value())


