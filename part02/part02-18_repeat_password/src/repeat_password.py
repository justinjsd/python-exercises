# Write your solution here
pasw = input("Password: ")
while True:
    repasw = input("Repeat password: ")
    if pasw != repasw:
        print("They do not match!")
    else:
        break
print("User account created!")
