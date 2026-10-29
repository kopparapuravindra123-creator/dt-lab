n = int(input("Enter number of expenses: "))
total = 0
largest = 0
largest_name = ""

for i in range(n):
    name = input("Enter expense category: ")
    amount = float(input("Enter foreign currency amount: "))
    rate = float(input("Enter exchange rate in Rs.: "))

    rupees = amount * rate
    fee = rupees * 0.02
    cost = rupees + fee

    total = total + cost

    if cost > largest:
        largest = cost
        largest_name = name

print("Total Travel Cost: Rs.", total)
print("Largest Expense:", largest_name)
print("Largest Expense Cost: Rs.", largest)

budget = float(input("Enter travel budget in Rs.: "))

if total <= budget:
    print("Within Budget")
else:
    print("Budget Exceeded")