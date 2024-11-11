# Write your solution here

word = input("Please type in a word: ")
char = input("Please type in a character: ")

index = int(word.find(char))

if index + 3 <= len(word):
    print(word[index:index+3])

