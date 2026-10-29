data_needed = float(input("Enter required data in GB: "))
budget = float(input("Enter your budget: "))

plans = [
    ("Plan A", 10, 199),
    ("Plan B", 20, 299),
    ("Plan C", 30, 399)
]

best_plan = ""
best_cost = float("inf")

for name, data, cost in plans:
    if data >= data_needed and cost <= budget:
        if cost < best_cost:
            best_cost = cost
            best_plan = name

if best_plan:
    print("Best Plan:", best_plan)
    print("Plan Cost: Rs.", best_cost)
else:
    print("No suitable plan found")