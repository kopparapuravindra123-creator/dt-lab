marks = float(input("Enter aggregate marks: "))
attendance = float(input("Enter attendance percentage: "))
income = float(input("Enter annual family income: "))

if marks >= 75 and attendance >= 75 and income <= 200000:
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")