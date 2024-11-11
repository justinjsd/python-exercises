# Write your solution here

from datetime import datetime, timedelta

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

current = datetime(year, month, day)
mill = datetime(1999, 12, 31)
age = mill - current

if age.days > 0:
    print(f"You were {age.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")