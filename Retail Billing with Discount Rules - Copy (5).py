n = int(input("Enter number of products: "))
total = 0

for i in range(n):
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    total += price * qty

if total >= 5000:
    discount = min(total * 0.10, 1000)
else:
    discount = 0

tax = total * 0.05
bill = total + tax - discount

print("Total:", total)
print("Discount:", discount)
print("Tax:", tax)
print("Final Bill:", bill)