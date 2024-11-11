# Write your solution here
n = int(input("Layers: "))
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#print(alphabet[n])
left = ""    # section, that goes downwards
right = ""    # section, that goes upwards
k = n-1       # the location of next character in alphabets
m = 2*n-1     # the number of characters in between
while k >= 1:
    left = left+alphabet[k]
    right = alphabet[k]+right
    m -= 2
    print(left+alphabet[k]*m+right)
    k -= 1

while k <= n-1:
    print(left+alphabet[k]*m+right)
    left = left[:-1]
    right = right[1:]
    m += 2
    k += 1