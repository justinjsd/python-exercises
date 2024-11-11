# Write your solution here

l = []
i = 0

while True:
    word = input("Word: ")
    if word in l:
        break
    l.append(word)
    i += 1

print(f"You typed in {i} different words")