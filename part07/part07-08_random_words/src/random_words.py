# Write your solution here

from random import *

def word_pool(file):
    word_pool = []
    with open(file) as words:
        for word in words:
            word = word.strip()
            word_pool.append(word)
    return word_pool

def words(n: int, beginning: str):
    beg_words = []
    for word in word_pool("words.txt"):
        if word.startswith(beginning):
            beg_words.append(word)
    return sample(beg_words, n)

if __name__ == "__main__":
    word_list = words(2, "car")
    for word in word_list:
        print(word)