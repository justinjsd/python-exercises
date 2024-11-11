# Write your solution here

word = input("Word: ")
char = input("Please type in a character: ")

while True:
    if len(word) < 3:
        break
    index = int(word.find(char))
    if index == -1 or len(word[index:]) < 3:
        break
    else:
        index + 3 <= len(word)
        print(word[index:index+3])
        word = word[index+1:]