from mip import Model, xsum, BINARY

# Set the number of doors and trucks
Nd = 3
Nt = 5

# Set the operations begin time
B = 0

# Create a model
model = Model()

# Define the decision variables
x = [[model.add_var(var_type=BINARY) for j in range(Nd)] for i in range(Nt)]

# Add the constraint Aij ≥ B for all i and j
for i in range(Nt):
    for j in range(Nd):
        model.add_constr(x[i][j] >= B)

# Set the objective function (example)
objective = xsum(x[i][j] for i in range(Nt) for j in range(Nd))

# Set the objective sense (minimize or maximize)
model.objective = objective

# Solve the model
model.optimize()

# Print the optimal solution
if model.status == 'OPTIMAL':
    print("Optimal Solution:")
    for i in range(Nt):
        for j in range(Nd):
            if x[i][j].x >= 0.99:  # Check if the variable is almost 1
                print(f"Truck {i+1} assigned to Door {j+1}")
else:
    print("No optimal solution found.")



