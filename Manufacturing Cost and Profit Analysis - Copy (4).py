material = float(input("Enter material cost: "))
labour = float(input("Enter labour cost: "))
machine = float(input("Enter machine cost: "))
quantity = int(input("Enter quantity produced: "))
price = float(input("Enter selling price per item: "))

total_cost = material + labour + machine
revenue = quantity * price
profit = revenue - total_cost

print("Total Cost:", total_cost)
print("Revenue:", revenue)
print("Profit:", profit)

if profit >= 5000:
    print("Profit Target Achieved")
else:
    print("Profit Target Not Achieved")