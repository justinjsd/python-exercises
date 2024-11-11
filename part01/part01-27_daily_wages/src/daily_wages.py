# Write your solution here
wage = float(input("Hourly wage: "))
hours = int(input("Hourly worked: "))
day = input("Day of the week: ")
if day == "Sunday":
    wages = 2 * wage * hours 
else:
    wages = wage * hours
print(f"Daily wages: {wages} euros")