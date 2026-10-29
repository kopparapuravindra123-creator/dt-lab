venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificates = float(input("Enter certificate cost: "))

sponsorship = float(input("Enter sponsorship amount: "))
fee = float(input("Enter registration fee per student: "))

total_cost = venue + equipment + catering + transport + certificates
shortfall = max(0, total_cost - sponsorship)

if sponsorship >= total_cost:
    minimum = 0
else:
    minimum = int(shortfall / fee)
    if shortfall % fee != 0:
        minimum = minimum + 1

print("Total Event Cost: Rs.", total_cost)
print("Sponsorship Shortfall: Rs.", shortfall)
print("Minimum Registrations:", minimum)

if sponsorship >= total_cost:
    print("Event Cost Fully Covered by Sponsorship")
else:
    print("Registration Needed to Cover Remaining Cost")