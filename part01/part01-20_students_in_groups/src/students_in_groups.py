# Write your solution here
stud = int(input("How many students on the course? "))
size = int(input("Desired group size? "))

groups = (stud + (size - 1)) // size

print(f"Number of groups formed: {groups}")