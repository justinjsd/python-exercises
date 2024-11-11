# Write your solution here

sentence = input("Please type in a sentence: ")

length = len(sentence)
n = 0
index = 0

while index > -1:
    print(sentence[0])
    index = sentence.find(" ")
    sentence = sentence[index+1:]