# Write your code here

from math import *

def hypotenuse(leg1: float, leg2: float):
    return sqrt(leg1**2 + leg2**2)

if __name__ == "__main__":
    hyp = hypotenuse(3,4)
    print(hyp)