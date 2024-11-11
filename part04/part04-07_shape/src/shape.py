# Copy here code of line function from previous exercise and use it in your solution
def line(n1, chara, n2, charb):
    a = 1
    b = 1
    while a <= n1:
        while b <= n1:
            print(chara*b)
            b += 1
        a += 1
    b -= 1
    a = 1
    while a <= n2:
        print(charb*b)
        a += 1

def shape(n1, chara, n2, charb):
    line(n1, chara, n2, charb)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")