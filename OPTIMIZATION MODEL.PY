# Install PuLP if not already installed
!pip install pulp --quiet

# Import PuLP library
import pulp

# ---------------------------
# Step 1: Define the Problem
# ---------------------------
# Create the LP problem instance: Maximize profit
prob = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)

# ---------------------------
# Step 2: Define Decision Variables
# ---------------------------
# Units of Product A and Product B to produce (cannot be negative)
product_A = pulp.LpVariable('Product_A', lowBound=0, cat='Continuous')
product_B = pulp.LpVariable('Product_B', lowBound=0, cat='Continuous')

# ---------------------------
# Step 3: Define Objective Function
# ---------------------------
# Maximize total profit = 40*Product A + 30*Product B
prob += 40*product_A + 30*product_B, "Total_Profit"

# ---------------------------
# Step 4: Define Constraints
# ---------------------------
# Machine 1: 2 hours for A + 1 hour for B ≤ 100
prob += 2*product_A + 1*product_B <= 100, "Machine_1_hours"

# Machine 2: 1 hour for A + 2 hours for B ≤ 80
prob += 1*product_A + 2*product_B <= 80, "Machine_2_hours"

# ---------------------------
# Step 5: Solve the Problem
# ---------------------------
prob.solve()

# ---------------------------
# Step 6: Display Solution
# ---------------------------
print("Status:", pulp.LpStatus[prob.status])
print(f"Optimal units of Product A: {product_A.varValue}")
print(f"Optimal units of Product B: {product_B.varValue}")
print(f"Maximum Profit: ${pulp.value(prob.objective)}")

# ---------------------------
# Step 7: Insights
# ---------------------------
print("\n--- Insights ---")
print("1. Produce units of A and B according to the solution above to maximize profit.")
print("2. This respects the available hours on Machine 1 and Machine 2.")
print("3. If machine hours or profits change, re-run the optimization to find new optimal quantities.")