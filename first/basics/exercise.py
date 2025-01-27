age: int = int(input("enter your age: "))

minAge: int = 18
maxAge: int = 45

if age < minAge:
    print("you're too young for this ride")
elif age > maxAge:
    print("you're too old for this ride")
else:
    print("enjoy the ride")
