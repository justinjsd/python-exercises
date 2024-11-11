# Write your solution here
first = int(input("Please type in the first number: "))
second = int(input("Please type in the second number: "))

if first > second:
    print(f"The greater number was: {first}")
elif second > first:
    print(f"The greater number was: {second}")
else:
    print("The numbers are equal!")