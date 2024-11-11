# write your solution here

sentence = input("Write text: ")

words = []

with open("wordlist.txt") as wordlist:
    for word in wordlist:
        word = word.replace("\n", "")
        word = word.split(",")
        words.append(word[0])

s_words =  sentence.split(" ")
i = 0
while i < len(s_words):
# for s_word in s_words:
    if s_words[i].lower() in words:
        s_words[i] = s_words[i]
    else:
        s_words[i] = f"*{s_words[i]}*"
    if i == len(s_words) - 1:
        print(f"{s_words[i]}")
    else:
        print(f"{s_words[i]} ", end="")
    i += 1