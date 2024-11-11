# Write your solution here

from random import *

def roll(side: str):
    a = [3, 3, 3, 3, 3, 6]
    b = [2, 2, 2, 5, 5, 5]
    c = [1, 4, 4, 4, 4, 4]

    if side == "A":
        return choice(a)
    elif side == "B":
        return choice(b)
    else:
        return choice(c)
    
def play(die1: str, die2: str, times: int):
    i = 0
    counter_1 = 0
    counter_2 = 0
    counter_tie = 0

    for i in range(times):
        rd1 = roll(die1) 
        rd2 = roll(die2) 
        if rd1 > rd2:
            counter_1 += 1
        elif rd1 < rd2:
            counter_2 += 1
    counter_tie = times - (counter_1 + counter_2)

    return (counter_1, counter_2, counter_tie)

if __name__ == "__main__":  
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()
    result = play("A", "B", 100)
    print(result)