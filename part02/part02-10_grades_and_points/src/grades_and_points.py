# Write your solution here
points = int(input("How many points [0-100]: "))
if points < 0:
    print(f"Grade: impossible!")
elif points < 50:
    print(f"Grade: fail")
elif points < 60:
    print(f"Grade: 1")
elif points < 70:
    print(f"Grade: 2")
elif points < 80:
    print(f"Grade: 3")
elif points < 90:
    print(f"Grade: 4")
elif points <= 100:
    print(f"Grade: 5")
else:
    print(f"Grade: impossible!")
