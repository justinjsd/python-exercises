# Write your solution here

counter = 1

while True:
    pin = input("PIN: ")
    if pin == "4321" and counter == 1:
        print("Correct! It only took you one single attempt!")
        break
    elif pin == "4321":
        print(f"Correct! It took you {counter} attempts")
        break
    else:
        print("Wrong")
        counter = counter+1

