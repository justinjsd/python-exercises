# Write your solution here
letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")

if (letter1 > letter2 and letter1 < letter3) or (letter1 < letter2 and letter1 > letter3):
    print(f"The letter in the middle is {letter1}")
elif (letter2 > letter1 and letter2 < letter3) or (letter2 < letter1 and letter2 > letter3):
    print(f"The letter in the middle is {letter2}")
else:
    print(f"The letter in the middle is {letter3}")