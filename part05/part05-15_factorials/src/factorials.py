# Write your solution here

def factorials(n: int):
    dick = {}
    fact = 1
    for i in range(1, n+1):
        fact *= i
        dick[i] = fact
    return dick

if __name__ == "__main__":
    k = factorials(5)
    print(k)