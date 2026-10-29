distance = float(input("Enter distance in km: "))
age = int(input("Enter passenger age: "))

fare = distance * 2

if age < 12:
    fare = fare * 0.50
elif age >= 60:
    fare = fare * 0.75

fare = fare + 20

print("Reservation Fee: Rs. 20")
print("Final Railway Fare: Rs.", fare)