# Write your solution here# Write your solution here
times = float(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
money = float(input("How much money do you spend on groceries in a week? "))

weekly = money + (price * times)

print("Average food expenditure:")
print(f"Weekly: {weekly} euros")
print(f"Daily: {weekly/7} euros")
