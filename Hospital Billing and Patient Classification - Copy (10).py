consultation = float(input("Enter consultation fee: "))
diagnostic = float(input("Enter diagnostic fee: "))
treatment = float(input("Enter treatment fee: "))
patient = input("Enter patient type (senior/normal): ")

total = consultation + diagnostic + treatment

if patient.lower() == "senior":
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

print("Total Bill: Rs.", total)
print("Discount: Rs.", discount)
print("Final Bill: Rs.", final_bill)

if final_bill <= 5000:
    print("Classification: Low Bill")
else:
    print("Classification: High Bill")