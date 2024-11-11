# Write your solution here

year = int(input("Year: "))

rem = year % 4
nextyear = year + (4-rem)

if year % 4 == 0:
    nextyear = year + 4
    
if nextyear % 100 == 0:
    if nextyear % 400 != 0:
        nextyear = nextyear + 4

print(f"The next leap year after {year} is {nextyear}")

