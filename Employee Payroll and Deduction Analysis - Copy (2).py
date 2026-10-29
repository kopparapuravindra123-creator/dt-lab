basic = float(input("Enter basic salary: "))
overtime = float(input("Enter overtime amount: "))
incentive = float(input("Enter incentive: "))

hra = basic * 0.20
gross = basic + hra + 1000 + overtime + incentive
deduction = gross * 0.10
net = gross - deduction

print("HRA:", hra)
print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net)