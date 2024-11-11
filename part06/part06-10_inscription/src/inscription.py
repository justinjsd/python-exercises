# Write your solution here

to = input("Whom should I sign this to: ")
file = input("Where shall I save it: ")

with open(file, "w") as file:
    file.write(f"Hi {to}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")