# Write your solution here
# (32°F − 32) × 5/9

ftemp = int(input("Please type in a temperature (F): "))
ctemp = float((ftemp - 32) * 5/9)
print(f"{ftemp} degrees Fahrenheit equals {ctemp} degrees Celsius")
if ctemp < 0:
    print("Brr! It's cold in here!")