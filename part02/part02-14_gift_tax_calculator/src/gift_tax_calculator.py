# Write your solution here

gift = int(input("Value of gift: "))

if gift < 5000:
    tax = 0
elif gift >= 5000 and gift < 25000:
    tax = (100 + (gift - 5000) * 0.08)
elif gift >= 25000 and gift < 55000:
    tax = (1700 + (gift - 25000) * 0.10)
elif gift >= 55000 and gift < 200000:
    tax = (4700 + (gift - 55000) * 0.12)
elif gift >= 200000 and gift < 1000000:
    tax = (22100 + (gift - 200000) * 0.15)
else:
    tax = (142100 + (gift - 1000000) * 0.17)

if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {float(tax)} euros")