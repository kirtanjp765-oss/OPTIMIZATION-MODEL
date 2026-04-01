# OPTIMIZATION-MODEL

*COMPANY*: Codtech IT Solutions Private Limited

*NAME*: Kirtan Jitendra Patel

*INTERN ID*: CTIS5909

*DOMAIN*: Data Science

*DURATION*: 4 Weeks

*MENTOR*: Neela Santhosh Kumar

*DESCRIPTION*:
In today’s competitive business environment, companies often face complex decision-making challenges, where they need to allocate limited resources in the most efficient way to maximize profit or minimize costs. One of the most widely used approaches for such problems is optimization techniques, particularly linear programming (LP). Linear programming is a mathematical method used to determine the best possible outcome for a given objective, while satisfying a set of constraints. This task focuses on using LP to solve a practical business problem and demonstrates its implementation using Python, specifically with the PuLP library, which is designed for linear optimization.

The business problem chosen for this task is a product mix optimization problem. In this scenario, a manufacturing company produces multiple products, each with different profit margins and resource requirements. The resources, such as machine hours, labor, or raw materials, are limited. The company’s goal is to decide how many units of each product to produce to maximize total profit while ensuring that the constraints of resource availability are not violated. This problem reflects a typical real-world situation faced by production managers, supply chain planners, and operational strategists.

The first step in solving this problem is defining the objective function. The objective function represents the business goal, which, in this case, is to maximize total profit. The profit for each product is calculated as the number of units produced multiplied by the profit per unit. Summing up the profits of all products forms the total profit, which becomes the target for maximization.

Next, the decision variables must be defined. Decision variables represent the quantities that the company can control—in this example, the number of units to produce for each product. These variables are constrained by physical and operational limits, such as the available machine hours. For instance, if Product A requires two hours on Machine 1 per unit and Product B requires one hour, the sum of the time allocated to all products cannot exceed the total available hours of Machine 1. Similar constraints are applied for other resources.

Once the objective function and constraints are clearly defined, the next step is formulating the problem mathematically. Linear programming models are constructed using linear relationships between the decision variables, objective function, and constraints. Each constraint ensures that resource usage stays within available limits, while the objective function guides the model toward the best outcome. This mathematical formulation is essential to translate the real-world problem into a solvable optimization model.

Python provides a robust framework for solving LP problems through libraries like PuLP. PuLP allows users to define variables, objective functions, and constraints programmatically and then use built-in solvers to find optimal solutions. In this task, the problem is implemented in Python using a combination of clear and structured code that defines decision variables, sets up the objective function, adds constraints, and solves the problem. After solving, the code outputs the optimal production quantities for each product and the maximum achievable profit.

Finally, interpreting the solution is critical for making actionable business decisions. The results inform the company about the optimal allocation of resources. For example, if the solution indicates producing 30 units of Product A and 25 units of Product B, the company can adjust production schedules, allocate labor and machines accordingly, and predict expected profits. Additionally, insights derived from the model can guide management decisions under changing conditions, such as variations in machine availability, labor costs, or product demand.

In conclusion, this task demonstrates the practical application of optimization techniques in business decision-making. It combines mathematical modeling, Python programming, and business insights to provide a structured approach for solving resource allocation problems. By implementing the product mix optimization using PuLP, users not only learn the technical process of linear programming but also develop a framework for analyzing and improving real-world operational efficiency. The deliverable—a Python notebook—serves as a complete demonstration of problem setup, solution, and insights, making it a valuable tool for both learning and practical business application.

*OUTPUT* :
